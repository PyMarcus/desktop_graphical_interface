from views import view_login
import sys


def load_system() -> None:
    success = view_login()
    print(success)
    if success:
        print('open_window')

    sys.exit(0)


if __name__ == '__main__':
    load_system()
