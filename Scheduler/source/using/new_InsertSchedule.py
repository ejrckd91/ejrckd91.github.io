#-*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\InsertSchedule.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from kdc_postgresql import Data_Scheduler as ds
class Ui_Schedule(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 50, 100, 30))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 50, 100, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(330, 50, 100, 30))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(30, 110, 400, 370))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 640, 100, 50))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.load_input_button)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 640, 100, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 100, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 100, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 100, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 640, 100, 50))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.read_sql_data)

        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(30, 510, 400, 100))
        self.textEdit_5.setObjectName("textEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "스케줄입력"))
        self.pushButton_2.setText(_translate("MainWindow", "스케줄삭제"))
        self.label.setText(_translate("MainWindow", "날짜입력"))
        self.label_2.setText(_translate("MainWindow", "중요도입력"))
        self.label_3.setText(_translate("MainWindow", "대표단어"))
        self.pushButton_3.setText(_translate("MainWindow", "확인"))

    def load_input_button(self):
        text_date = self.textEdit.toPlainText()
        text_rank = self.textEdit_2.toPlainText()
        text_val = self.textEdit_3.toPlainText()
        text_schedule = self.textEdit_4.toPlainText()
        ##스케쥴내용을 바로 DB에 입력했을 때 띄어쓰기나 이런게 사용이 될까모르겠다
        ##안된다면 스케쥴 내용은 텍스트 파일로 만들어서 따로 저장하고 저장되는 멤버는 그 텍스트 위치로 하는게 어떨까

        ##sql문 실행을 위해서 내가 만든 class를 임폴트 해두었으니 사용하기
        if(text_date!=""):
            self.textEdit_5.append(text_date)
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()

        ds.Insert_data(text_date,text_rank,text_val,text_schedule)

    def read_sql_data(self):##list는 초기화하고 돌릴때 append로하기 꼭 데이터베이스에서 리스트로 받아오는데 이중리스트라 그안의것은 튜플임
        text_date = self.textEdit.toPlainText()
        i = 0
        j = 0
        text_search = []
        res = ds.Read_data(text_date)
        self.textEdit_5.clear()
        for j in range(0,len(res)):
            text_search.append(("{0} {1} {2} {3}").format(str(res[j][0]),str(res[j][1]),res[j][2],res[j][3]))
            self.textEdit_5.insertPlainText(("{0}\n").format(text_search[j]))
            ##if(text_search[j]==['']):
                ##self.textEdit_5.insertPlainText("end") 이부분 구현이 잘 안되네

    #def delete_sql_data():##삭제가 고민된다. 맘같아서는 읽어왔을 때 나온것을 클릭하면 그 정보가 임시저장되서 삭제를 누르면 삭제되게 하고싶다
                          ##어차피 순서가 정해져있는 db라서 리드로 읽어온것들의 데이터를 받아두는것도 좋을 듯하다. 그럼 전역변수에??
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Schedule()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
