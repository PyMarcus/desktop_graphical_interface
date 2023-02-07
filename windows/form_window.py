from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PySide6.QtGui import QFont
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setMinimumHeight(400)
        self.setMinimumWidth(400)
        self.setMaximumWidth(1000)
        self.setMaximumHeight(700)
        #self.setGeometry(200, 200, 250, 300)  # x,y,w,h
        self.setWindowTitle("Login Form")
        self.create_form()

    def create_form(self) -> None:
        font = QFont('../fonts/NTR-Regular.ttf')
        font.setPointSize(11)
        # name
        label_name = QLabel('Name', self)
        label_name.move(20, 20)
        label_name.setFont(font)

        space = QLineEdit(self)
        space.move(20, 50)
        space.setFont(font)
        space.setPlaceholderText('Name')

        # password
        label_password = QLabel('Password', self)
        label_password.move(20, 80)
        label_password.setFont(font)

        space2 = QLineEdit(self)
        space2.move(20, 110)
        space2.setFont(font)
        space2.setPlaceholderText('Password')
        space2.setEchoMode(QLineEdit.EchoMode.Password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
    sys.exit(0)
