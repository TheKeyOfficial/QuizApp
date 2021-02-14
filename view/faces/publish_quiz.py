from ..interfaces import MenuInterface
from control import GameManager


class PublishQuiz(MenuInterface):
    PUBLIC = 'Public'
    PRIVATE = 'Private'
    QUIZ_TITLE = 'Please enter a title for your Quiz: '

    def __init__(self, title='\nPUBLISH QUESTION\n'):
        super().__init__(title=title)
        self.game_manager = GameManager.instance()
        self.USER_MENU = {self.PUBLIC: self.public_dialog,
                          self.PRIVATE: self.private_dialog}
        self.active_menu = self.USER_MENU
        self.show()
        pass

    def public_dialog(self):
        title = input(self.QUIZ_TITLE)
        self.game_manager.create_public_quiz(title)
        pass

    def private_dialog(self):
        title = input(self.QUIZ_TITLE)
        self.game_manager.create_private_quiz(title)
        pass
