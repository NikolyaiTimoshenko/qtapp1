import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from one import Ui_first  # Импортируем класс Ui_first из one.py
from second import Ui_second  # Импортируем класс Ui_second из second.py


class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_first()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_window2)  # Ищет кнопку и при ее нажатии открывает второе окно

    def open_window2(self):
        self.window2 = Window2()
        self.window2.show()
        self.hide()


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_second()
        self.ui.setupUi(self)
        self.ui.label.mousePressEvent = self.go_back_to_window1
        self.ui.pushButton.clicked.connect(self.write_button_text_to_file)  # Ищет текст и при ее нажатии открывает
        # первое окно

    def go_back_to_window1(self, event):
        self.window1 = Window1()
        self.window1.show()
        self.hide()

    def write_button_text_to_file(self):
        # Получаем текст кнопки и записываем его в файл
        button_text = self.ui.pushButton.text()

        # Путь к файлу, в который нужно записать текст
        file_path = "F:\GabiTask\output.txt"

        # Открываем файл для записи в режиме добавления (если файла нет, он будет создан)
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(button_text + '\n')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = Window1()
    window1.show()
    sys.exit(app.exec_())
