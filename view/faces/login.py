from ..interfaces import FaceInterface


from utilities import check_credentials


class Login(FaceInterface):
    GET_NAME = 'Name: '
    GET_PASSWORD = 'Password: '

    def __init__(self, title='\nLOGIN'):
        super().__init__(title=title)
        self.show()
        pass

    def show(self):
        """
        Display a Login terminal.
        :return: name, password
        """
        print(self.TITLE)
        try:
            name = self.get_name().lower()
            password = self.get_password()
            self.user_manager.login(name, password)
        except Exception as e:
            print(e)
        pass

    def get_name(self) -> str:
        """
        Function to get the name from terminal input
        :return: user input
        """
        # get name as input
        name = input(self.GET_NAME)
        # checks if input contains a space or is empty
        if check_credentials(name):
            return name

    def get_password(self) -> str:
        """
        Function to get the password from terminal input
        :return: user input
        """
        # get password as input
        password = input(self.GET_PASSWORD)
        # checks if input contains a space or is empty
        if check_credentials(password):
            return password


