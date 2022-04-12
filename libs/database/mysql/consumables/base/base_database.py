import os

import pymysql

from libs.utils import get_logger


class BaseDataBase:
    def __init__(self):
        self.__connect()

    def __connect(self):
        self._connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            db=os.getenv("MYSQL_DB"),
            port=int(os.getenv("MYSQL_PORT")),
        )

    def ping(self):
        self._connection.ping(reconnect=True)

    def __del__(self):
        self._connection.close()
