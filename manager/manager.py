from views import view_login, start
import sys


def load_system() -> None:
    success = view_login()
    if success:
        start()
    sys.exit(0)


if __name__ == '__main__':
    load_system()
