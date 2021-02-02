from ..interfaces import MenuInterface


class AddQuestion(MenuInterface):
    CHOICE_QUESTION = 'Choice question'
    NUMBER_QUESTION = 'Number question'
    TEXT_QUESTION = 'Text question'

    QUESTION = 'Enter a question text: '
    CHOICE = 'Add a choice (type \'q\' to quit): '
    CHOICE_SOLUTION = 'What is the index of the solution: '
    SOLUTION = 'What is the solution: '

    def __init__(self, title='\nCREATE QUESTION\n'):
        super().__init__(title=title)
        self.USER_MENU = {self.CHOICE_QUESTION: self.choice_question_dialog,
                          self.NUMBER_QUESTION: self.number_question_dialog,
                          self.TEXT_QUESTION: self.text_question_dialog,
                          self.EXIT: self.quit()}
        self.active_menu = self.USER_MENU
        self.show()
        pass

    def choice_question_dialog(self):
        question_text = input(self.QUESTION)
        choices = []
        loop = True
        while loop:
            user_input = input(self.CHOICE)
            if user_input != 'q':
                choices.append(user_input)
            else:
                loop = False
        solution = int(input(self.CHOICE_SOLUTION))
        if solution <= len(choices):
            self.game_manager.create_question(question_txt=question_text, choices=choices, solution=solution)
        pass

    def number_question_dialog(self):
        question_text = input(self.QUESTION)
        solution = int(input(self.SOLUTION))
        self.game_manager.create_question(question_txt=question_text, solution=solution)
        pass

    def text_question_dialog(self):
        question_text = input(self.QUESTION)
        solution = input(self.SOLUTION)
        self.game_manager.create_question(question_txt=question_text, solution=solution)
        pass
