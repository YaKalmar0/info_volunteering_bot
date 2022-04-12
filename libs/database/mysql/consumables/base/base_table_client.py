from pymysql.connections import Connection
from pymysql.cursors import Cursor


class BaseTableClient:
    def __init__(self, connection: Connection) -> None:
        self._connection = connection
