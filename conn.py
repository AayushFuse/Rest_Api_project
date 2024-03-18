import sqlite3


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, 
                                        cls).__call__(*args, **kwds)

        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonType):
    def __init__(self, db_name="students") -> None:
        self.__conn = sqlite3.connect(f"{db_name}.db")

    def get_cursor(self):
        return self.__conn


# print(DatabaseConnection() is DatabaseConnection())
