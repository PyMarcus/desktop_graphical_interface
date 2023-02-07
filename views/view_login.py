from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
from PySide6.QtGui import QFont, QIcon
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(400, 600)
        self.setWindowTitle('Syscad :: Login')
        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color: #FFFFFF')
        self.__define_form()

    def __define_form(self) -> None:
        font = QFont('../fonts/NTR-Regular.ttf')
        font.setPointSize(11)

        # username
        text_user = QLineEdit(self)
        text_user.setPlaceholderText('Username')
        text_user.setFont(font)
        text_user.setGeometry(10, 240, 381, 41)

        # password
        text_pass = QLineEdit(self)
        text_pass.setPlaceholderText('Password')
        text_pass.setFont(font)
        text_pass.setGeometry(10, 320, 381, 41)
        text_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.__define_button(font)
        self.__define_images()

    def __define_button(self, font: QFont) -> QPushButton:
        login = QPushButton('Login', self)
        login.setFont(font)
        login.setGeometry(10, 390, 381, 41)
        login.setStyleSheet(
            'background-color: #1E90FF;'
            'color: #FFFFFF;'
            'font-weight:bold;')
        return login

    def __define_images(self) -> None:
        app_icon = QIcon('../images/app.svg')
        self.setWindowIcon(app_icon)
        login_icon = QIcon('../images/user.svg')

        pixmap_logo = login_icon.pixmap(191, 191)

        label_logo = QLabel('Logo', self)
        label_logo.setPixmap(pixmap_logo)
        label_logo.move(100, 10)


def view_login() -> None:
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    view_login()
    sys.exit(0)
