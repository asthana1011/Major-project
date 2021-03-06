# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'q_msg.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
Dialog = ""
class Ui_Dialog(object):
    q_name = ""
    ok_flag = 0
    def init(self):
        global Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.setModal(True)
        Dialog.exec_()
        Dialog.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(608, 108)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color: rgb(43, 36, 91);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_2.setStyleSheet("background-color: rgb(43, 36, 91);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color: rgb(43,36,91);\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(49, 128, 255);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ok_btn = QtWidgets.QPushButton(self.frame_3)
        self.ok_btn.setEnabled(True)
        self.ok_btn.setMinimumSize(QtCore.QSize(0, 20))
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout_2.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.frame_3)
        self.cancel_btn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.cancel_btn.setObjectName("cancel_btn")
        self.verticalLayout_2.addWidget(self.cancel_btn)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)

        self.ok_btn.clicked.connect(self.handle_qaction)
        self.cancel_btn.clicked.connect(self.handle_cancelAction)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Queue Name"))
        self.label.setText(_translate("Dialog", "Queue Name:"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
        self.cancel_btn.setText(_translate("Dialog", "Cancel"))

    def handle_qaction(self):
        Ui_Dialog.q_name = self.lineEdit.text()
        if Ui_Dialog.q_name != "":
            Ui_Dialog.ok_flag = 1
            global Dialog
            Dialog.close()

    def handle_cancelAction(self):
        Dialog.close()
        Ui_Dialog.q_name = ""
        



    