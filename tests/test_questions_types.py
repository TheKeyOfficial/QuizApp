from unittest import TestCase
from model.quiz.question import *


class TestQuestionTypes(TestCase):
    def test_choice_answer(self):
        question = ChoiceQuestion('What is 1-1?', choices=['1', '0', '2'], solution=1)
        self.assertTrue(question.answer(1))

    def test_number_answer(self):
        question = NumberQuestion('What is 1-1?', solution=0)
        self.assertTrue(question.answer(0))

    def test_text_answer(self):
        question = TextQuestion('What is 1-1?', solution='0')
        self.assertTrue(question.answer('0'))

