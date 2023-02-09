from typing import Any, Sequence
import mysql.connector as mc
import configparser as cp
from mysql.connector import MySQLConnection


class ReportDAO:

    @staticmethod
    def read_config():
        path = 'C:\\Users\\Marcu\\Documents\\settings.cfg'
        parser = cp.RawConfigParser()
        parser.read(path)
        return parser['development']

    @staticmethod
    def connection() -> MySQLConnection | None:
        try:
            conn = mc.connect(host=ReportDAO.read_config().get('host'),
                              user=ReportDAO.read_config().get('user'),
                              db=ReportDAO.read_config().get('database'),
                              )
            return conn
        except ConnectionError as e:
            pass

    @staticmethod
    def select_all() -> tuple[Sequence[Any], list[str | int | None | bool]]:
        with ReportDAO.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clients;")
            result = cursor.fetchall()
            size = len(cursor.description)  # columns
            titles = [title[0] for title in cursor.description]
            return result, titles


if __name__ == '__main__':
    ...
