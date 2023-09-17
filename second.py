#файл второго окна

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal


class Ui_second(object):
    label_clicked = pyqtSignal()
    def setupUi(self, second):
        second.setObjectName("second")
        second.resize(300, 300)
        second.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(second)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 245, 33))
        self.pushButton.setStyleSheet("color: rgb(31, 27, 255);\n"
"background-color: rgb(238, 238, 238);\n"
"border-radius: 13px;                     /* <----  20px  */ \n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 210, 245, 33))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"background-color: rgb(31, 27, 255);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 13px; /* Закругленные углы, если нужно */\n"
"}\n"
"/*color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 183, 140);\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"/*border: 2px solid #094065;")
        #тут есть лишние css параметры,
        #которые почему то не отображаются в QtDesigner
        self.label.setObjectName("label")
        second.setCentralWidget(self.centralwidget)

        self.retranslateUi(second)
        QtCore.QMetaObject.connectSlotsByName(second)

    def retranslateUi(self, second):
        _translate = QtCore.QCoreApplication.translate
        second.setWindowTitle(_translate("second", "MainWindow"))
        self.pushButton.setText(_translate("second", "Говно в текстовом документе"))
        self.label.setText(_translate("second", "<--НАЗАД"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    second = QtWidgets.QMainWindow()
    ui = Ui_second()
    ui.setupUi(second)
    second.show()
    sys.exit(app.exec_())
