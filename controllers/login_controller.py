from PySide6.QtWidgets import QLineEdit


class LoginController:

    @staticmethod
    def validate_login(user: QLineEdit, password: QLineEdit) -> bool:
        if user == 'admin' and password == 'password':
            return True
        return False
