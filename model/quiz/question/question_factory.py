from desing_pattern import Factory
from model.quiz.question import *


class QuestionFactory(Factory):
    CHOICES = 'choices'
    SOLUTION = 'solution'

    def __init__(self):
        super().__init__()
        pass

    def make(self, question_txt: str, **kwargs):
        if self.check_if_choice_question(**kwargs):
            return ChoiceQuestion(question_txt, choices=kwargs.get(self.CHOICES), solution=kwargs.get(self.SOLUTION))

        if self.check_if_number_question(**kwargs):
            return NumberQuestion(question_txt, solution=kwargs.get(self.SOLUTION))

        if self.check_if_text_question(**kwargs):
            return TextQuestion(question_txt, solution=kwargs.get(self.SOLUTION))
        pass

    def check_if_choice_question(self, **kwargs) -> bool:
        return self.CHOICES in kwargs.keys()

    def check_if_number_question(self, **kwargs) -> bool:
        return self.SOLUTION in kwargs.keys() and type(kwargs.get(self.SOLUTION)) == int

    def check_if_text_question(self, **kwargs) -> bool:
        return self.SOLUTION in kwargs.keys() and type(kwargs.get(self.SOLUTION)) == str
