from PySide6.QtWidgets import QApplication, QWidget
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
    sys.exit(0)
