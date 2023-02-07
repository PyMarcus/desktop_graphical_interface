from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QLabel, QLineEdit
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('Syscad :: Main')
        self.setGeometry(300, 300, 1000, 700)
        app_icon = QIcon('../images/app.svg')
        self.setWindowIcon(app_icon)
        self.setStyleSheet('background-color: #1E90FF;')
        self.__define_form()

    def __define_form(self) -> None:
        global frame_register, frame_search, frame_report, frame_edit
        font = QFont('../fonts/NTR-Regular.ttf')
        font.setPointSize(11)

        # register
        button_register = QPushButton('Register', self)
        button_register.setFont(font)
        button_register.setGeometry(0, 0, 170, 50)
        button_register.setStyleSheet('background-color: #FFFFFF;'
                                      'color:#1E90FF;'
                                      'font-weight:bold;')
        button_register.clicked.connect(self.__show_register_frame)

        # search
        button_search = QPushButton('Search', self)
        button_search.setFont(font)
        button_search.setGeometry(0, 50, 170, 50)
        button_search.setStyleSheet('background-color: #FFFFFF;'
                                      'color:#1E90FF;'
                                      'font-weight:bold;')
        button_search.clicked.connect(self.__show_search_frame)


        # report
        button_report = QPushButton('Report', self)
        button_report.setFont(font)
        button_report.setGeometry(0, 100, 170, 50)
        button_report.setStyleSheet('background-color: #FFFFFF;'
                                      'color:#1E90FF;'
                                      'font-weight:bold;')
        button_report.clicked.connect(self.__show_report_frame)


        # edit
        button_edit = QPushButton('Edit', self)
        button_edit.setFont(font)
        button_edit.setGeometry(0, 150, 170, 50)
        button_edit.setStyleSheet('background-color: #FFFFFF;'
                                      'color:#1E90FF;'
                                      'font-weight:bold;')
        button_edit.clicked.connect(self.__show_edit_frame)

        # register frame
        frame_register = QFrame(self)
        frame_register.setGeometry(170, 0, 830, 700)
        frame_register.setStyleSheet('background-color: #FFFFFF')
        frame_register.setVisible(False)

        label_name = QLabel('Name', frame_register)
        label_name.setGeometry(20, 50, 55, 16)
        label_name.setFont(font)

        label_address = QLabel('Address', frame_register)
        label_address.setGeometry(20, 90, 55, 16)
        label_address.setFont(font)

        label_cpf = QLabel('CPF', frame_register)
        label_cpf.setGeometry(20, 130, 55, 16)
        label_cpf.setFont(font)

        text_name = QLineEdit(frame_register)
        text_name.setFont(font)
        text_name.setGeometry(80, 50, 721, 22)

        text_address = QLineEdit(frame_register)
        text_address.setFont(font)
        text_address.setGeometry(80, 90, 721, 22)

        text_cpf = QLineEdit(frame_register)
        text_cpf.setFont(font)
        text_cpf.setGeometry(80, 130, 721, 22)

        button_clear = QPushButton('Clear', frame_register)
        button_clear.setFont(font)
        button_clear.setGeometry(20, 650, 115, 22)

        button_register = QPushButton('Register', frame_register)
        button_register.setFont(font)
        button_register.setGeometry(700, 650, 115, 22)



        # search frame
        frame_search = QFrame(self)
        frame_search.setGeometry(170, 0, 830, 700)
        frame_search.setStyleSheet('background-color: green')
        frame_search.setVisible(False)

        # report frame
        frame_report = QFrame(self)
        frame_report.setGeometry(170, 0, 830, 700)
        frame_report.setStyleSheet('background-color: red')
        frame_report.setVisible(False)

        # edit frame
        frame_edit = QFrame(self)
        frame_edit.setGeometry(170, 0, 830, 700)
        frame_edit.setStyleSheet('background-color: blue')
        frame_edit.setVisible(False)

        global frames

        frames = (frame_register, frame_report, frame_search, frame_edit)

    @staticmethod
    def __hidden_frames() -> None:
        global frames

        for frame in frames:
            if frame.isVisible():
                frame.setVisible(False)

    def __show_register_frame(self) -> None:
        global frame_register

        self.__hidden_frames()
        frame_register.setVisible(True)

    def __show_search_frame(self) -> None:
        global frame_search

        self.__hidden_frames()
        frame_search.setVisible(True)

    def __show_report_frame(self) -> None:
        global frame_report

        self.__hidden_frames()
        frame_report.setVisible(True)

    def __show_edit_frame(self) -> None:
        global frame_edit

        self.__hidden_frames()
        frame_edit.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
    sys.exit(0)
