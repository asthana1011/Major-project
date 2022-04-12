from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QPropertyAnimation, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import master_ui,q_msg, load_q, database
import os
from gestures import pause_play as pp


count = 0
flag = 0
dur = 0
pos = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = master_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.q_db = database.q_controls()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.ui.screen)

        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.ui.slider.sliderMoved.connect(self.setSliderPosition)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        self.ui.volumeSlider.sliderMoved.connect(self.changeVolume)
        self.ui.volumeSlider.setValue(30)

        self.ui.play.setShortcut("space")
        self.ui.stop.setShortcut("w")
        self.ui.rewind.setShortcut("a")
        self.ui.forward.setShortcut("d")

        self.ui.menu_btn.clicked.connect(self.handle_menu)
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.exit.clicked.connect(lambda:self.close())
        self.ui.openmed.clicked.connect(self.open_media)
        self.ui.savemed.clicked.connect(self.save_media)
        self.ui.exitapp.clicked.connect(lambda:self.close())
        self.ui.playmed.clicked.connect(self.play_media)
        self.ui.pausemed.clicked.connect(self.play_media)
        self.ui.stopmed.clicked.connect(self.stop_media)
        self.ui.frwdmed.clicked.connect(self.forward_media)
        self.ui.rewmed.clicked.connect(self.rewind_media)
        self.ui.nextmed.clicked.connect(self.next_media)
        self.ui.prevmed.clicked.connect(self.previous_media)
        self.ui.gesture.clicked.connect(self.gesture_mode)
        self.ui.openqueue.clicked.connect(self.open_queue)
        self.ui.crque.clicked.connect(self.create_queue)
        self.ui.delque.clicked.connect(self.delete_queue)
        self.ui.usage.clicked.connect(self.user_manual)
        self.ui.winhelp.clicked.connect(self.windows_help)
        self.ui.rewind.clicked.connect(self.rewind_media)
        self.ui.forward.clicked.connect(self.forward_media)
        self.ui.play.clicked.connect(self.play_media)
        self.ui.stop.clicked.connect(self.stop_media)


        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.title_bar.mouseMoveEvent = moveWindow
        self.show()
        
    def mousePressEvent(self, event):
        global count
        count += 1
        if count == 2:
            self.restore_or_maximize_window()
            count = 0
        self.clickPosition = event.globalPos()
        
        
    def handle_menu(self):
        width = self.ui.frame_6.width()
        #minimzed
        if width == 15:
            new_width = 120
        else:   #maximized
            new_width = 15
        #animate
        self.animation = QPropertyAnimation(self.ui.frame_6,b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.maximize.setIcon(QtGui.QIcon("icons/icons8-maximize-window-100.png"))
        else:
            self.showMaximized()
            self.ui.maximize.setIcon(QtGui.QIcon("icons/icons8-restore-window-100.png"))

    def open_media(self):
        filename, _ =QFileDialog.getOpenFileName(caption = "Select file",filter="(*.wmv *.mkv *.mp3 *.mp4)")
        
        tail = os.path.split(filename)
        if filename != '':
            self.ui.nowplaying.setText("Now Playing: "+tail[1])
            self.mediaPlayer.setVolume(30)
            global flag
            flag = 1
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.mediaPlayer.play()
            self.ui.play.setIcon(QtGui.QIcon("icons/icons8-pause-90.png"))

    def save_media(self):
        pass


    def play_media(self):
        global flag 
        if flag != 0:
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                self.mediaPlayer.pause()
                self.ui.play.setIcon(QtGui.QIcon("icons/icons8-play-90.png"))
            else:
                self.mediaPlayer.play()
                self.ui.play.setIcon(QtGui.QIcon("icons/icons8-pause-90.png")) 

    def stop_media(self):
        self.mediaPlayer.stop()
        self.ui.play.setIcon(QtGui.QIcon("icons/icons8-play-90.png"))

    def setSliderPosition(self, position):
        self.mediaPlayer.setPosition(position)
    def positionChanged(self, position):
        self.ui.slider.setValue(position)
    def durationChanged(self, duration):
        self.ui.slider.setRange(0, duration)


    def forward_media(self, position):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 10000)
    def rewind_media(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 10000)
    def changeVolume(self):
        if self.ui.volumeSlider.value() < 5:
            self.mediaPlayer.setMuted(1)
        else:
            self.mediaPlayer.setMuted(0)
            self.mediaPlayer.setVolume(self.ui.volumeSlider.value())

    def next_media(self):
        pass
    def previous_media(self):
        pass
    def gesture_mode(self):
        pp.cam()

    def open_queue(self):
        w = load_q.Ui_Dialog()
        w.init()
        if w.ok_flag == 1:
            files = self.q_db.show_contents(w.queue_name)
            global flag
            flag = 1
            for filename in files:
                tail = os.path.split(filename)
                self.mediaPlayer.setVolume(30)
                print(filename)
                self.ui.nowplaying.setText("Now Playing: "+tail[1])
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
                self.mediaPlayer.play()
                self.ui.play.setIcon(QtGui.QIcon("icons/icons8-pause-90.png"))


    def create_queue(self):
        w = q_msg.Ui_Dialog()
        w.init()
        if w.ok_flag == 1:
            filename, _ =QFileDialog.getOpenFileName(caption = "Select file",filter="(*.wmv *.mkv *.mp3 *.mp4)")
            self.q_db.create_new_queue(w.q_name)
            self.q_db.update_queue(w.q_name, filename)
            #self.q_db.show_queue()
            #self.q_db.show_contents()

    def delete_queue(self):
        w = load_q.Ui_Dialog()
        w.init()
        print(w.queue_name)
        if w.queue_name != "":
            self.q_db.drop_queue(w.queue_name)

    def user_manual(self):
        pass
    def windows_help(self):
        pass
    
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Window = MainWindow()
    sys.exit(app.exec_())