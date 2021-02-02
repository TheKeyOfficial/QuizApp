from typing import Final
from ..interfaces import DataManagerInterface
from . import User, RegisteredUser, IdleUser
from utilities import check_password, hash_password
from desing_pattern import Singleton
import re


@Singleton
class UserDataManager(DataManagerInterface):
    # const
    LOGIN_DATA: Final = 'login_data'
    PASSWORD_REGEX: Final = r'[A-Za-z0-9@#$%^&+=]{4,}'

    def __init__(self):
        """
        this class permits interaction with the user data.
        """
        super().__init__()
        pass

    @staticmethod
    def get_new_user() -> IdleUser:
        """
        get new user -> idle user
        :return: IdleUser
        """
        return IdleUser()

    @staticmethod
    def get_new_registered_user(name: str, password: str) -> RegisteredUser:
        """
        get new RegisteredUser
        :param name: name of the user
        :param password: password of the user
        :return: new RegisteredUser
        """
        return RegisteredUser(name=name, password=hash_password(password))

    def add_user(self, reg_user: RegisteredUser) -> None:
        """
        add a user to database
        :param reg_user: user to add
        :return: None
        """
        # ger data from database and convert reg_user to dict
        data = self.database_manager.read_database()
        reg_user_dict = reg_user.__dict__()
        try:
            # first try to add user to login_data
            data[self.LOGIN_DATA].update(reg_user_dict)
        except Exception:
            # if no 'login_data' key exists in json data create first
            data.update({self.LOGIN_DATA: reg_user_dict})
        # write updates to database
        self.database_manager.write_database(data)
        pass

    def get_user(self, name: str, password: str) -> RegisteredUser:
        """
        get user from database by name and password
        :param name: string
        :param password: string
        :return: if user exist return RegisteredUser
        """
        # get data from database
        data = self.database_manager.read_database()
        # get user from data
        user = data[self.LOGIN_DATA][name]
        # check if user.password == password. If true return new RegisteredUser from user data
        if check_password(user['password'], password):
            return RegisteredUser(name, **user)
        raise Exception

    def user_exist(self, user: RegisteredUser) -> bool:
        """
        checks if a user wit the same name exist
        :param user: User to check if exist
        :return: True if user exists
        """
        # get data from database
        data = self.database_manager.read_database()
        try:
            # select just the login data
            login_data = data[self.LOGIN_DATA]
            # check login_data contains the user. If not KeyError will raise
            if login_data[user.name] is not None:
                return True
        except KeyError:
            return False

    @staticmethod
    def is_registered_user(user: User) -> bool:
        """
        checks if user is registered
        :param user: user to check
        :return: True if registered else False
        """
        if type(user) is RegisteredUser:
            return True
        else:
            return False

    def password_requirements(self, password: str) -> bool:
        if re.fullmatch(self.PASSWORD_REGEX, password):
            return True
        return False
