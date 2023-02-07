from typing import Any, Tuple

import mysql.connector as mc
from contextlib import contextmanager
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
    @contextmanager
    def connection() -> MySQLConnection | None:
        try:
            conn = mc.connect(host=ReportDAO.read_config().get('host'),
                              user=ReportDAO.read_config().get('user'),
                              db=ReportDAO.read_config().get('database'),
                              )
            try:
                yield conn
            except Exception as e:
                print(e)
            finally:
                conn.commit()
                conn.close()
        except ConnectionError as e:
            print(e)

    @staticmethod
    def select_all() -> Tuple[str | Any] | None:
        with ReportDAO.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clients;")
            result = cursor.fetchall()
            size = len(cursor.description)  # columns
            titles = [title[0] for title in cursor.description]
            for lines in result:
                yield lines, size, titles


if __name__ == '__main__':
    for n, s, t in ReportDAO.select_all():
        print(n, s, t)
