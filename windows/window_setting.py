from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QIcon, QPixmap
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('GUI application')
        # self.setGeometry()  #x, y, w, h
        self.setMinimumHeight(400)
        self.setMinimumWidth(400)
        self.setMaximumWidth(1000)
        self.setMaximumHeight(700)
        self.setToolTip('Login window')
        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color: #FFFFFF;')

        window_icon = QIcon('../images/login_icon.png')
        self.setWindowIcon(window_icon)
        self.__set_image()

    def __set_image(self) -> None:
        """
        Create icons on screen
        :return:
        """
        icon_check = QIcon('../images/check.png')
        label_name = QLabel('Name', self)
        pixmap_icon_check = icon_check.pixmap(50, 50, QIcon.Active)
        label_name.setPixmap(pixmap_icon_check)

        icon_check_disabled = QIcon('../images/check.png')
        label_name_disabled = QLabel('Name', self)
        pixmap_icon_check_disabled = icon_check_disabled.pixmap(50, 50, QIcon.Disabled)
        label_name_disabled.setPixmap(pixmap_icon_check_disabled)

        icon_check_selected = QIcon('../images/check.png')
        label_name_selected = QLabel('Name', self)
        pixmap_icon_check_selected = icon_check_selected.pixmap(50, 50, QIcon.Selected)
        label_name_selected.setPixmap(pixmap_icon_check_selected)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
    sys.exit(0)
