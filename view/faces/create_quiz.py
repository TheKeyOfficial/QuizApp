from ..interfaces import MenuInterface
from .add_question import AddQuestion
from .publish_quiz import PublishQuiz


class CreateQuiz(MenuInterface):
    ADD_QUESTION = 'Add Question'
    PUBLISH = 'Publish'
    NUM_QUESTIONS = 'Number of added questions (min 3, max 10): '

    def __init__(self, title='\nCREATE QUIZ:\n'):
        super().__init__(title=title)
        self.USER_MENU = {self.ADD_QUESTION: self.add_question_dialog, self.EXIT: self.quit}
        self.active_menu = self.USER_MENU

        self.show()
        pass

    def build_menu(self):
        question_buffer_size = self.game_manager.get_question_buffer_len()
        self.TITLE = f'\nCREATE QUIZ:\n' \
                     f'Number of added questions (min 3, max 10): {question_buffer_size}\n'
        self.clear_menu()
        if question_buffer_size >= 3:
            self.active_menu.update({self.PUBLISH: self.publish_question_dialog})
        self.build_menu_items()
        pass

    def add_question_dialog(self) -> None:
        """
        show add question dialog
        :return: None
        """
        # start add question dialog
        AddQuestion()
        # after adding a question show create quiz user menu
        self.show()
        pass

    def publish_question_dialog(self) -> None:
        """
        show publish quiz dialog
        :return: None
        """
        # start publish quiz dialog
        PublishQuiz()
        # after publishing the quiz show end dialog
        pass
