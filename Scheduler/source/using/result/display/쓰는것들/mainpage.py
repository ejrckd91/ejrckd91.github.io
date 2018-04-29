# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(955, 500)
        self.frame_display = QtWidgets.QFrame(Dialog)
        self.frame_display.setGeometry(QtCore.QRect(-1, -1, 551, 501))
        self.frame_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_display.setObjectName("frame_display")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_display)
        self.graphicsView.setGeometry(QtCore.QRect(20, 120, 511, 271))
        self.graphicsView.setObjectName("graphicsView")
        self.textEdit = QtWidgets.QTextEdit(self.frame_display)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_display)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 50, 104, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_display)
        self.textEdit_3.setGeometry(QtCore.QRect(270, 50, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.frame_display_2 = QtWidgets.QFrame(Dialog)
        self.frame_display_2.setGeometry(QtCore.QRect(549, -1, 411, 501))
        self.frame_display_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_display_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_display_2.setObjectName("frame_display_2")
        self.label = QtWidgets.QLabel(self.frame_display_2)
        self.label.setGeometry(QtCore.QRect(60, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_buttons = QtWidgets.QFrame(self.frame_display_2)
        self.frame_buttons.setGeometry(QtCore.QRect(0, 60, 411, 441))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.D_day_Box = QtWidgets.QTextBrowser(self.frame_buttons)
        self.D_day_Box.setGeometry(QtCore.QRect(110, 10, 281, 41))
        self.D_day_Box.setObjectName("D_day_Box")
        self.D_1_Box = QtWidgets.QTextBrowser(self.frame_buttons)
        self.D_1_Box.setGeometry(QtCore.QRect(110, 70, 281, 41))
        self.D_1_Box.setObjectName("D_1_Box")
        self.D_2_Box = QtWidgets.QTextBrowser(self.frame_buttons)
        self.D_2_Box.setGeometry(QtCore.QRect(110, 130, 281, 41))
        self.D_2_Box.setObjectName("D_2_Box")
        self.D_3_Box = QtWidgets.QTextBrowser(self.frame_buttons)
        self.D_3_Box.setGeometry(QtCore.QRect(110, 190, 281, 41))
        self.D_3_Box.setObjectName("D_3_Box")
        self.D_4_Box = QtWidgets.QTextBrowser(self.frame_buttons)
        self.D_4_Box.setGeometry(QtCore.QRect(110, 250, 281, 41))
        self.D_4_Box.setObjectName("D_4_Box")
        self.D_5_Box = QtWidgets.QTextBrowser(self.frame_buttons)
        self.D_5_Box.setGeometry(QtCore.QRect(110, 310, 281, 41))
        self.D_5_Box.setObjectName("D_5_Box")
        self.D_day = QtWidgets.QLabel(self.frame_buttons)
        self.D_day.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.D_day.setAlignment(QtCore.Qt.AlignCenter)
        self.D_day.setObjectName("D_day")
        self.D_1 = QtWidgets.QLabel(self.frame_buttons)
        self.D_1.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.D_1.setAlignment(QtCore.Qt.AlignCenter)
        self.D_1.setObjectName("D_1")
        self.D_2 = QtWidgets.QLabel(self.frame_buttons)
        self.D_2.setGeometry(QtCore.QRect(10, 140, 81, 21))
        self.D_2.setAlignment(QtCore.Qt.AlignCenter)
        self.D_2.setObjectName("D_2")
        self.D_3 = QtWidgets.QLabel(self.frame_buttons)
        self.D_3.setGeometry(QtCore.QRect(10, 200, 81, 21))
        self.D_3.setAlignment(QtCore.Qt.AlignCenter)
        self.D_3.setObjectName("D_3")
        self.D_4 = QtWidgets.QLabel(self.frame_buttons)
        self.D_4.setGeometry(QtCore.QRect(10, 260, 81, 21))
        self.D_4.setAlignment(QtCore.Qt.AlignCenter)
        self.D_4.setObjectName("D_4")
        self.D_5 = QtWidgets.QLabel(self.frame_buttons)
        self.D_5.setGeometry(QtCore.QRect(10, 320, 81, 21))
        self.D_5.setAlignment(QtCore.Qt.AlignCenter)
        self.D_5.setObjectName("D_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_buttons)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 360, 411, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_add_Scehdule = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_add_Scehdule.setObjectName("pushButton_add_Scehdule")
        self.horizontalLayout.addWidget(self.pushButton_add_Scehdule)
        self.pushButton_Alarm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Alarm.setObjectName("pushButton_Alarm")
        self.horizontalLayout.addWidget(self.pushButton_Alarm)
        self.pushButton_Prev = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Prev.setObjectName("pushButton_Prev")
        self.horizontalLayout.addWidget(self.pushButton_Prev)

        self.retranslateUi(Dialog)
        self.pushButton_add_Scehdule.clicked.connect(self.frame_display.show)
        self.pushButton_Alarm.clicked.connect(self.frame_display.show)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "일정 표시"))
        self.D_day_Box.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">중요도/시간/요약내용 표기</p></body></html>"))
        self.D_1_Box.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.D_2_Box.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.D_3_Box.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.D_4_Box.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.D_5_Box.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.D_day.setText(_translate("Dialog", "D-day"))
        self.D_1.setText(_translate("Dialog", "D-1"))
        self.D_2.setText(_translate("Dialog", "D-2"))
        self.D_3.setText(_translate("Dialog", "D-3"))
        self.D_4.setText(_translate("Dialog", "D-4"))
        self.D_5.setText(_translate("Dialog", "D-5"))
        self.pushButton_add_Scehdule.setText(_translate("Dialog", "일정추가"))
        self.pushButton_Alarm.setText(_translate("Dialog", "알람설정"))
        self.pushButton_Prev.setText(_translate("Dialog", "지난일정"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

