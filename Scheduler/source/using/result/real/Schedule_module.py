# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Schedule_module.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(680, 662)
        Form.setAutoFillBackground(True)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 680, 700))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 678, 698))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(70, 30, 70, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 70, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(370, 30, 70, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(520, 30, 70, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit.setGeometry(QtCore.QRect(30, 65, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit.setDate(QtCore.QDate(1999, 1, 1))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(200, 65, 120, 30))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_2.setGeometry(QtCore.QRect(350, 65, 120, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_3.setGeometry(QtCore.QRect(500, 65, 120, 30))
        self.textEdit_3.setObjectName("textEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(30, 120, 600, 411))
        self.plainTextEdit_4.setMouseTracking(True)
        self.plainTextEdit_4.setTabletTracking(True)
        self.plainTextEdit_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(30, 580, 120, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 580, 120, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 580, 120, 35))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 580, 120, 35))
        self.pushButton_4.setObjectName("pushButton_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.dateTimeEdit, self.plainTextEdit_4)
        Form.setTabOrder(self.plainTextEdit_4, self.scrollArea)
        Form.setTabOrder(self.scrollArea, self.textEdit_3)
        Form.setTabOrder(self.textEdit_3, self.textEdit_2)
        Form.setTabOrder(self.textEdit_2, self.textEdit)
        Form.setTabOrder(self.textEdit, self.pushButton)
        Form.setTabOrder(self.pushButton, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.pushButton_3)
        Form.setTabOrder(self.pushButton_3, self.pushButton_4)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "D-day"))
        self.label_2.setText(_translate("Form", "주제"))
        self.label_3.setText(_translate("Form", "중요도"))
        self.label_4.setText(_translate("Form", "비고"))
        self.dateTimeEdit.setDisplayFormat(_translate("Form", "yyyyMMddhhmm"))
        self.pushButton.setText(_translate("Form", "스케쥴조회"))
        self.pushButton_2.setText(_translate("Form", "스케쥴입력"))
        self.pushButton_3.setText(_translate("Form", "스케쥴삭제"))
        self.pushButton_4.setText(_translate("Form", "나가기"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
