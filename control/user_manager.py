from model import UserDataManager
from desing_pattern import Singleton


@Singleton
class UserManager(object):
    def __init__(self):
        self.user_data_manager = UserDataManager.instance()
        self.user = self.user_data_manager.get_new_user()
        pass

    def login(self, name: str, password: str):
        try:
            self.user = self.user_data_manager.get_user(name=name, password=password)
        except Exception:
            raise Exception('Wrong login data!')
        pass

    def logout(self):
        """
        logs out the current user
        :return:
        """
        # overwrite user in database with current user date
        self.user_data_manager.add_user(self.user)
        # set current user to new user
        self.user = self.user_data_manager.get_new_user()
        pass

    def register(self, name: str, password: str) -> None:
        """
        registers a new user to the database.
        if successful, then set current user to newly registered user
        :param name: name of the new user -> Exception if name already exists
        :param password: the password of the new user -> min 4 chars
        :return: None
        """
        # create new registered user
        reg_user = self.user_data_manager.get_new_registered_user(name, password)

        # check if new reg_user exists in the database and if the password is at least 4 chars long.
        # send Error notifications back to mainloop ExceptionHandling
        if self._check_new_user_credentials(reg_user, password) is True:
            self.user_data_manager.add_user(reg_user)
            # set current user to reg_user
            self.user = reg_user
        pass

    def _check_new_user_credentials(self, reg_user, plain_password) -> bool:
        """
        checks if the user name already exists and if the password requirements are correct
        :param reg_user: user who does not yet exist in the database
        :param plain_password: cleartext password
        :return: True if credentials are correct else Exception for mainloop ExceptionHandling
        """
        if self.user_data_manager.user_exist(reg_user) is not True:
            if self.user_data_manager.password_requirements(plain_password):
                return True
            else:
                raise Exception('A password must consist of at least 4 characters!')
        else:
            raise Exception("Sorry this username is already taken.")

    def is_registered_user(self) -> bool:
        """
        checks if user is registered
        :return: True if registered else False
        """
        return self.user_data_manager.is_registered_user(self.user)
