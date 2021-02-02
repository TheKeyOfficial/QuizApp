from abc import ABC
from ..database_manager import DatabaseManager


class DataManagerInterface(ABC):
    def __init__(self):
        self.database_manager = DatabaseManager.instance()
        pass
