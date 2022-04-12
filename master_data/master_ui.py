# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chk1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.centralwidget)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.title_bar.setStyleSheet("background-color: rgb(43, 36, 91);")
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menubuton = QtWidgets.QHBoxLayout()
        self.menubuton.setSpacing(0)
        self.menubuton.setObjectName("menubuton")
        self.menu_btn = QtWidgets.QPushButton(self.title_bar)
        self.menu_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.menu_btn.setStyleSheet("QPushButton{\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color:rgb(43,36,91);\n"
"    color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgb(49, 128, 255);\n"
"}")
        self.menu_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../exps/icons/icons8-menu-384.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setObjectName("menu_btn")
        self.menubuton.addWidget(self.menu_btn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.menubuton)
        self.videoname = QtWidgets.QHBoxLayout()
        self.videoname.setObjectName("videoname")
        self.nowplaying = QtWidgets.QLabel(self.title_bar)
        self.nowplaying.setStyleSheet("color:white")
        self.nowplaying.setObjectName("nowplaying")
        self.videoname.addWidget(self.nowplaying, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addLayout(self.videoname)
        self.windowcontrols = QtWidgets.QHBoxLayout()
        self.windowcontrols.setSpacing(0)
        self.windowcontrols.setObjectName("windowcontrols")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.windowcontrols.addItem(spacerItem)
        self.minimize = QtWidgets.QPushButton(self.title_bar)
        self.minimize.setMaximumSize(QtCore.QSize(30, 16777215))
        self.minimize.setStyleSheet("QPushButton{\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color:rgb(43,36,91);\n"
"    color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : rgb(0,0,0);\n"
"    \n"
"}")
        self.minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../exps/icons/icons8-minimize-window-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize.setIcon(icon1)
        self.minimize.setObjectName("minimize")
        self.windowcontrols.addWidget(self.minimize, 0, QtCore.Qt.AlignLeft)
        self.maximize = QtWidgets.QPushButton(self.title_bar)
        self.maximize.setMaximumSize(QtCore.QSize(30, 16777215))
        self.maximize.setStyleSheet("QPushButton{\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color:rgb(43,36,91);\n"
"    color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"    \n"
"}")
        self.maximize.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../exps/icons/icons8-maximize-window-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize.setIcon(icon2)
        self.maximize.setObjectName("maximize")
        self.windowcontrols.addWidget(self.maximize, 0, QtCore.Qt.AlignRight)
        self.exit = QtWidgets.QPushButton(self.title_bar)
        self.exit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.exit.setStyleSheet("QPushButton{\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color:rgb(43,36,91);\n"
"    color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgb(255,0,0);\n"
"}")
        self.exit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../exps/icons/icons8-close-window-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon3)
        self.exit.setObjectName("exit")
        self.windowcontrols.addWidget(self.exit, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addLayout(self.windowcontrols)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addWidget(self.title_bar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_6.setStyleSheet("background-color: rgb(43, 36, 91);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(9, 9, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.side_menu = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy)
        self.side_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.side_menu.setMaximumSize(QtCore.QSize(120, 16777215))
        self.side_menu.setStyleSheet("QFrame{\n"
"background-color: rgb(43, 36, 91);\n"
"}\n"
"QPushButton{\n"
"   \n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color:rgb(43,36,91);\n"
"    color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgb(49, 128, 255);\n"
"}")
        self.side_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu.setObjectName("side_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.side_menu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.toolBox = QtWidgets.QToolBox(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.toolBox.setStyleSheet("QToolBox::tab {\n"
"   \n"
"    background-color: rgb(43, 36, 91);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    font: italic;\n"
"    color: white;\n"
"}")
        self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox.setLineWidth(0)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 91, 393))
        self.page.setStyleSheet("")
        self.page.setObjectName("page")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 95, 111))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgb(43, 36, 91);\n"
"}\n"
"QPushButton{\n"
"   \n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color:rgb(43,36,91);\n"
"    color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgb(49, 128, 255);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.openmed = QtWidgets.QPushButton(self.frame_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../exps/icons/icons8-opened-folder-480.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openmed.setIcon(icon4)
        self.openmed.setObjectName("openmed")
        self.verticalLayout_7.addWidget(self.openmed)
        self.savemed = QtWidgets.QPushButton(self.frame_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../exps/icons/icons8-save-all-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savemed.setIcon(icon5)
        self.savemed.setObjectName("savemed")
        self.verticalLayout_7.addWidget(self.savemed)
        self.exitapp = QtWidgets.QPushButton(self.frame_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../exps/icons/icons8-delete-480.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitapp.setIcon(icon6)
        self.exitapp.setObjectName("exitapp")
        self.verticalLayout_7.addWidget(self.exitapp)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../exps/icons/icons8-file-480.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon7, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 91, 393))
        self.page_2.setStyleSheet("")
        self.page_2.setObjectName("page_2")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 101, 221))
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color: rgb(43, 36, 91);\n"
"}\n"
"QPushButton{\n"
"   \n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color:rgb(43,36,91);\n"
"    color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgb(49, 128, 255);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.playmed = QtWidgets.QPushButton(self.frame_3)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../exps/icons/icons8-play-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playmed.setIcon(icon8)
        self.playmed.setObjectName("playmed")
        self.verticalLayout_8.addWidget(self.playmed)
        self.pausemed = QtWidgets.QPushButton(self.frame_3)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../exps/icons/icons8-pause-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pausemed.setIcon(icon9)
        self.pausemed.setObjectName("pausemed")
        self.verticalLayout_8.addWidget(self.pausemed)
        self.stopmed = QtWidgets.QPushButton(self.frame_3)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../exps/icons/icons8-stop-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopmed.setIcon(icon10)
        self.stopmed.setObjectName("stopmed")
        self.verticalLayout_8.addWidget(self.stopmed)
        self.frwdmed = QtWidgets.QPushButton(self.frame_3)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../exps/icons/icons8-fast-forward-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frwdmed.setIcon(icon11)
        self.frwdmed.setObjectName("frwdmed")
        self.verticalLayout_8.addWidget(self.frwdmed)
        self.rewmed = QtWidgets.QPushButton(self.frame_3)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../exps/icons/icons8-rewind-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rewmed.setIcon(icon12)
        self.rewmed.setObjectName("rewmed")
        self.verticalLayout_8.addWidget(self.rewmed)
        self.nextmed = QtWidgets.QPushButton(self.frame_3)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../exps/icons/icons8-end-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextmed.setIcon(icon13)
        self.nextmed.setObjectName("nextmed")
        self.verticalLayout_8.addWidget(self.nextmed)
        self.prevmed = QtWidgets.QPushButton(self.frame_3)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../exps/icons/icons8-skip-to-start-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevmed.setIcon(icon14)
        self.prevmed.setObjectName("prevmed")
        self.verticalLayout_8.addWidget(self.prevmed)
        self.gesture = QtWidgets.QPushButton(self.frame_3)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../exps/icons/icons8-hand-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gesture.setIcon(icon15)
        self.gesture.setObjectName("gesture")
        self.verticalLayout_8.addWidget(self.gesture)
        self.toolBox.addItem(self.page_2, icon8, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 91, 393))
        self.page_5.setObjectName("page_5")
        self.frame_4 = QtWidgets.QFrame(self.page_5)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 95, 111))
        self.frame_4.setStyleSheet("QFrame{\n"
"background-color: rgb(43, 36, 91);\n"
"}\n"
"QPushButton{\n"
"   \n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color:rgb(43,36,91);\n"
"    color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgb(49, 128, 255);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.openqueue = QtWidgets.QPushButton(self.frame_4)
        self.openqueue.setIcon(icon4)
        self.openqueue.setObjectName("openqueue")
        self.verticalLayout_9.addWidget(self.openqueue)
        self.crque = QtWidgets.QPushButton(self.frame_4)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../exps/icons/icons8-music-480.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.crque.setIcon(icon16)
        self.crque.setObjectName("crque")
        self.verticalLayout_9.addWidget(self.crque)
        self.delque = QtWidgets.QPushButton(self.frame_4)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../exps/icons/icons8-delete-bin-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delque.setIcon(icon17)
        self.delque.setObjectName("delque")
        self.verticalLayout_9.addWidget(self.delque)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("../exps/icons/icons8-music-library-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_5, icon18, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 91, 393))
        self.page_6.setObjectName("page_6")
        self.frame_5 = QtWidgets.QFrame(self.page_6)
        self.frame_5.setGeometry(QtCore.QRect(10, 0, 84, 81))
        self.frame_5.setStyleSheet("QFrame{\n"
"background-color: rgb(43, 36, 91);\n"
"}\n"
"QPushButton{\n"
"   \n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color:rgb(43,36,91);\n"
"    color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgb(49, 128, 255);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.usage = QtWidgets.QPushButton(self.frame_5)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("../exps/icons/icons8-business-documentation-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.usage.setIcon(icon19)
        self.usage.setObjectName("usage")
        self.verticalLayout_10.addWidget(self.usage)
        self.winhelp = QtWidgets.QPushButton(self.frame_5)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("../exps/icons/icons8-information-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.winhelp.setIcon(icon20)
        self.winhelp.setObjectName("winhelp")
        self.verticalLayout_10.addWidget(self.winhelp)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("../exps/icons/icons8-help-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_6, icon21, "")
        self.verticalLayout_6.addWidget(self.toolBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addWidget(self.side_menu)
        self.horizontalLayout.addWidget(self.frame_6)
        self.screen = QVideoWidget(self.centralwidget)
        #self.screen.setStyleSheet("background-color: rgb(0, 0, 0);")
        #self.screen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.screen.setFrameShadow(QtWidgets.QFrame.Raised)

        self.screen.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.screen.setStyleSheet('background-color: black')
        
        self.screen.setObjectName("screen")
        self.horizontalLayout.addWidget(self.screen)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.control_bar = QtWidgets.QFrame(self.centralwidget)
        self.control_bar.setMaximumSize(QtCore.QSize(16777215, 60))
        self.control_bar.setStyleSheet("QFrame{\n"
"    background-color:rgb(43,36,91);\n"
"}")
        self.control_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control_bar.setObjectName("control_bar")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.control_bar)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.media_control = QtWidgets.QFrame(self.control_bar)
        self.media_control.setMaximumSize(QtCore.QSize(120, 16777215))
        self.media_control.setStyleSheet("QFrame{\n"
"background-color: rgb(43, 36, 91);\n"
"}")
        self.media_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.media_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.media_control.setObjectName("media_control")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.media_control)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rewind = QtWidgets.QPushButton(self.media_control)
        self.rewind.setStyleSheet("QPushButton:hover{\n"
"background-color : rgb(49, 128, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color:rgb(43,36,91);\n"
"color : rgb(255,255,255);\n"
"}")
        self.rewind.setText("")
        self.rewind.setIcon(icon12)
        self.rewind.setObjectName("rewind")
        self.horizontalLayout_2.addWidget(self.rewind)
        self.play = QtWidgets.QPushButton(self.media_control)
        self.play.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
" padding: 5px;\n"
" background-color:rgb(43,36,91);\n"
"color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(49,128,255);\n"
"}")
        self.play.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("../exps/icons/icons8-play-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon22)
        self.play.setObjectName("play")
        self.horizontalLayout_2.addWidget(self.play)
        self.forward = QtWidgets.QPushButton(self.media_control)
        self.forward.setStyleSheet("QPushButton:hover{\n"
"background-color : rgb(49, 128, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color:rgb(43,36,91);\n"
"color : rgb(255,255,255);\n"
"}")
        self.forward.setText("")
        self.forward.setIcon(icon11)
        self.forward.setObjectName("forward")
        self.horizontalLayout_2.addWidget(self.forward)
        self.horizontalLayout_2.setStretch(0, 9)
        self.horizontalLayout_2.setStretch(2, 9)
        self.horizontalLayout_6.addWidget(self.media_control)
        self.seek_bar = QtWidgets.QFrame(self.control_bar)
        self.seek_bar.setStyleSheet("QFrame{\n"
"    background-color: rgb(43, 36, 91);\n"
"}")
        self.seek_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seek_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seek_bar.setObjectName("seek_bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.seek_bar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slider = QtWidgets.QSlider(self.seek_bar)
        self.slider.setStyleSheet("QSlider{\n"
"    background-color: rgb(43, 36, 91);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    \n"
"    background-color: rgb(240, 240, 240);\n"
"    border-radius: 4px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(49, 171, 16);\n"
"    border: 2px; \n"
"    width: 11px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 5px; \n"
"    }\n"
"QSlider::handle:horizontal:hover{\n"
"    background-color: rgb(170, 0, 255);\n"
"}")
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.verticalLayout_2.addWidget(self.slider)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.timer = QtWidgets.QFrame(self.seek_bar)
        self.timer.setStyleSheet("background-color: rgb(43, 36, 91);")
        self.timer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer.setObjectName("timer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.timer)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.volumeSlider = QtWidgets.QSlider(self.timer)
        self.volumeSlider.setStyleSheet("QSlider{\n"
"    background-color: rgb(43, 36, 91);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    \n"
"    background-color: rgb(240, 240, 240);\n"
"    border-radius: 4px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(49, 171, 16);\n"
"    border: 2px; \n"
"    width: 11px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 5px; \n"
"    }\n"
"QSlider::handle:horizontal:hover{\n"
"    background-color: rgb(170, 0, 255);\n"
"}")
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_5.addWidget(self.volumeSlider)
        spacerItem1 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.stop = QtWidgets.QPushButton(self.timer)
        self.stop.setMaximumSize(QtCore.QSize(30, 16777215))
        self.stop.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
" padding: 5px;\n"
" background-color:rgb(43,36,91);\n"
"color : rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(49,128,255);\n"
"}")
        self.stop.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("../exps/icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon23)
        self.stop.setObjectName("stop")
        self.horizontalLayout_5.addWidget(self.stop)
        self.timetamp = QtWidgets.QLabel(self.timer)
        self.timetamp.setStyleSheet("")
        self.timetamp.setObjectName("timetamp")
        self.horizontalLayout_5.addWidget(self.timetamp)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addWidget(self.timer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6.addWidget(self.seek_bar)
        self.verticalLayout.addWidget(self.control_bar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nowplaying.setText(_translate("MainWindow", "YouControl: Gesture Controlled Media Player"))
        self.openmed.setText(_translate("MainWindow", "Open Media"))
        self.savemed.setText(_translate("MainWindow", "Save Media"))
        self.exitapp.setText(_translate("MainWindow", "Exit"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "File"))
        self.playmed.setText(_translate("MainWindow", "Play"))
        self.pausemed.setText(_translate("MainWindow", "Pause"))
        self.stopmed.setText(_translate("MainWindow", "Stop"))
        self.frwdmed.setText(_translate("MainWindow", "Forward"))
        self.rewmed.setText(_translate("MainWindow", "Rewind"))
        self.nextmed.setText(_translate("MainWindow", "Next"))
        self.prevmed.setText(_translate("MainWindow", "Previous"))
        self.gesture.setText(_translate("MainWindow", "Gesture Mode"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Playback"))
        self.openqueue.setText(_translate("MainWindow", "Load Queue"))
        self.crque.setText(_translate("MainWindow", "Create Queue"))
        self.delque.setText(_translate("MainWindow", "Erase Current"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("MainWindow", "Library"))
        self.usage.setText(_translate("MainWindow", "Usage"))
        self.winhelp.setText(_translate("MainWindow", "Window"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("MainWindow", "Help"))
        self.timetamp.setText(_translate("MainWindow", "--.--/--.--"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())