from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.create_button()

    def __action_callback(self) -> None:
        print('clicked')
        self.__message_box()

    def __message_box(self):
        info = QMessageBox.question(self, 'Confirmed', 'Congratulations', QMessageBox.Yes | QMessageBox.No)
        if info == QMessageBox.Yes:
            print('yes')
        else:
            print('No')

    def create_button(self) -> None:
        button = QPushButton('Ok', self)
        button.move(50, 120)
        button.clicked.connect(self.__action_callback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
    sys.exit(0)
