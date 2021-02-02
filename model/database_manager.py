import json
from desing_pattern import Singleton


@Singleton
class DatabaseManager(object):
    _instance = None
    DATABASE_PATH = "model/database.json"

    def __init__(self):
        pass

    def read_database(self) -> dict:
        with open(self.DATABASE_PATH, "r") as data_file:
            json_data = json.load(data_file)
            return json_data
        pass

    def write_database(self, data: dict):
        with open(self.DATABASE_PATH, "w") as data_file:
            json.dump(data, data_file, indent=4)
        pass
