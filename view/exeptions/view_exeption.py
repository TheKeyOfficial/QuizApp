class SpaceInUserName(Exception):
    def __init__(self, message='A username does not contain a space!'):
        self.message = message
        super().__init__(self.message)


class EmptyUserName(Exception):
    def __init__(self, message='The username can not be empty!'):
        self.message = message
        super().__init__(self.message)


class EmptyPassword(Exception):
    def __init__(self, message='The password can not be empty!'):
        self.message = message
        super().__init__(self.message)


class InvalidInput(Exception):
    def __init__(self, message='Invalid input pls try again.'):
        self.message = message
        super().__init__(self.message)
