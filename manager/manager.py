from views import view_login


def load_system() -> None:
    success = view_login()
    if success:
        print('open_window')