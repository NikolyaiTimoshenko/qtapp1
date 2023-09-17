#файл первого окна

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_first(object):
    def setupUi(self, first):
        first.setObjectName("first")
        first.resize(300, 299)
        first.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(first)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 245, 33))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
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
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 150, 245, 33))
        self.pushButton.setStyleSheet("color: rgb(31, 27, 255);\n"
"background-color: rgb(238, 238, 238);\n"
"border-radius: 13px;                     /* <----  20px  */ \n"
"")
        self.pushButton.setObjectName("pushButton")
        first.setCentralWidget(self.centralwidget)

        self.retranslateUi(first)
        QtCore.QMetaObject.connectSlotsByName(first)

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        first.setWindowTitle(_translate("first", "MainWindow"))
        self.label.setText(_translate("first", "СГЭУ"))
        self.pushButton.setText(_translate("first", "Передать что то куда то"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    first = QtWidgets.QMainWindow()
    ui = Ui_first()
    ui.setupUi(first)
    first.show()
    sys.exit(app.exec_())
