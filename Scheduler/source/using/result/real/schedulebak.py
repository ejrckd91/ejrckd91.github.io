# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Schedule_module.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from kdc_postgresql import Data_Scheduler as ds


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

        self.pushButton.clicked.connect(self.read_sql_data)

        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 580, 120, 35))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.load_input_button)

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



#####text_date 손봐야함
    def load_input_button(self):
        #text_now = self.d 현재시간을 구하는 것 새로 위에서 만들어야 할거같음.
        text_date = self.dateTimeEdit.dateTime().toPyDateTime() ##숫자부분만뽑아서넣는작업필요
        text_sub = self.textEdit.toPlainText()
        text_rank = self.textEdit_2.toPlainText()
        text_etc = self.textEdit_3.toPlainText()
        text_schedule = self.plainTextEdit_4.toPlainText()
        ##스케쥴내용을 바로 DB에 입력했을 때 띄어쓰기나 이런게 사용이 될까모르겠다
        ##안된다면 스케쥴 내용은 텍스트 파일로 만들어서 따로 저장하고 저장되는 멤버는 그 텍스트 위치로 하는게 어떨까

        ##sql문 실행을 위해서 내가 만든 class를 임폴트 해두었으니 사용하기
        if(text_date!=""):
            self.plainTextEdit_4.appendPlainText(str(text_date)) ##21번째꺼부터 받아오기
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.plainTextEdit_4.clear()

        ds.Insert_data(text_date,text_sub,text_rank,text_etc,text_schedule)#여기도 하나 추가해야하긴함

    def read_sql_data(self):##list는 초기화하고 돌릴때 append로하기 꼭 데이터베이스에서 리스트로 받아오는데 이중리스트라 그안의것은 튜플임
        text_date = self.dateTimeEdit.time(self)
        i = 0
        j = 0
        text_search = []
        res = ds.Read_data(text_date)
        self.plainTextEdit_4.clear()
        for j in range(0,len(res)):
            text_search.append(("{0} {1} {2} {3}").format(str(res[j][0]),str(res[j][1]),res[j][2],res[j][3]))
            self.plainTextEdit_4.insertPlainText(("{0}\n").format(text_search[j]))
            ##if(text_search[j]==['']):
                ##self.textEdit_5.insertPlainText("end") 이부분 구현이 잘 안되네

    #def delete_sql_data():##삭제가 고민된다. 맘같아서는 읽어왔을 때 나온것을 클릭하면 그 정보가 임시저장되서 삭제를 누르면 삭제되게 하고싶다
                          ##어차피 순서가 정해져있는 db라서 리드로 읽어온것들의 데이터를 받아두는것도 좋을 듯하다. 그럼 전역변수에??

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
