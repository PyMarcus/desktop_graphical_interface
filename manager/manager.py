from PySide6.QtWidgets import QApplication
from views import view_login, Window
import sys


def load_system() -> None:
    success = view_login()
    if success:
        print('ok')

    sys.exit(0)


if __name__ == '__main__':
    load_system()
