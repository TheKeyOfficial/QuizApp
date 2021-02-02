from ..interfaces import FaceInterface


class Logout(FaceInterface):
    DEMAND = 'Are you sure? (y/n): '

    def __init__(self, title='\nLOGOUT'):
        super().__init__(title=title)
        self.show()
        pass

    def show(self) -> None:
        """
        asks if the user is sure
        :return: None
        """
        # print title and wait for user input
        print(self.TITLE)
        selection = input(self.DEMAND)
        # if user inputs equals 'y' for 'yes' than change user to default user
        if selection == 'y':
            self.user_manager.logout()
        pass
