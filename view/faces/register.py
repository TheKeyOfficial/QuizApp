from .login import Login


class Register(Login):
    GET_NAME = 'Please enter your name: '
    GET_PASSWORD = 'Please enter your password: '

    def __init__(self, title='\nREGISTER'):
        super().__init__(title=title)
        pass

    def show(self):
        """
        Display a Login terminal.
        :return: name, password
        """
        print(self.TITLE)
        name = self.get_name()
        password = self.get_password()
        try:
            self.user_manager.register(name, password)
        except Exception as e:
            print(e)
        pass
