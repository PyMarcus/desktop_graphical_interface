from ctypes import Union
from typing import Any
import PySide6
from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide2.QtGui import QColor


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None) -> None:
        super().__init__()

        self.__data = data[0]
        self.__columns = data[1]
        self.__load_data(data)

    def __load_data(self, data) -> None:
        self.__number_rows = len(data[0])
        self.__number_columns = len(data[1])

    def rowCount(self, parent=QModelIndex()) -> int:
        return self.__number_rows

    def columnCount(self, parent=QModelIndex()) -> int:
        return self.__number_columns

    def data(self, index, role: int = ...) -> Any:
        column = index.column()
        row = index.row()
        try:
            if role == Qt.DisplayRole:
                return self.__data[row][column]
            elif role == Qt.TextAlignmentRole:
                if column == 0:
                    return Qt.AlignCenter
                return Qt.AlignLeft
            elif role == Qt.BackgroundRole:
                if row % 2 == 0:
                    return QColor(Qt.lightGray)
                return QColor(Qt.white)
        except IndexError as e:
            pass
        return None

    def headerData(self, section: int, orientation: Any, role: int = ...) -> Any:
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            try:
                return self.__columns[section]
            except IndexError as e:
                pass
        else:
            return section


if __name__ == '__main__':
    CustomTableModel()


