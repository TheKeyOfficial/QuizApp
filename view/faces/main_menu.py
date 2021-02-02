from ..interfaces import MenuInterface

from .login import Login
from .logout import Logout
from .register import Register
from .play_menu import PlayMenu
from .create_quiz import CreateQuiz
from .statistic import Statistic


class MainMenu(MenuInterface):
    LOGIN = 'Login'
    LOGOUT = 'Logout'
    REGISTER = 'Register'
    PLAY = 'Play quiz'
    CREATE_QUIZ = 'Create new quiz'
    STATISTIC = 'Show my statistics'

    USER_MENU = {LOGIN: Login, REGISTER: Register, PLAY: PlayMenu, STATISTIC: Statistic}
    REGISTERED_USER_MENU = {LOGOUT: Logout, PLAY: PlayMenu, CREATE_QUIZ: CreateQuiz, STATISTIC: Statistic}

    def __init__(self, title='WELCOME TO QUIZAPP'):
        super().__init__(title=title)
        self.active_menu = self.USER_MENU
        self.show()
        pass

    def build_menu(self):
        self.clear_menu()
        if self.user_manager.is_registered_user():
            self.TITLE = f'\nHELLO {self.user_manager.user.name} WELCOME TO QUIZAPP\n'
            self.active_menu = self.REGISTERED_USER_MENU
        else:
            self.TITLE = '\nWELCOME TO QUIZAPP\n'
            self.active_menu = self.USER_MENU
        self.build_menu_items()
        pass
