from libs.utils import get_logger

from .mysql import DataBase

logger = get_logger("mysql-setup")
logger.info("Initializing MySQL connection")
db = DataBase()
