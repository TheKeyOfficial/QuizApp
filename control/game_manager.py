from desing_pattern import Singleton
from model import QuestionFactory, Quiz, QuizDataManager, QUESTION_TYPES, UserQuiz

from .user_manager import UserManager


@Singleton
class GameManager(object):
    def __init__(self):
        self._quiz_data_manager = QuizDataManager.instance()
        self._question_factory = QuestionFactory()
        self._user_manager = UserManager.instance()
        self._question_buffer = []
        pass

    def create_private_quiz(self, title):
        quiz = Quiz(title, questions=self._question_buffer)
        user_quiz = UserQuiz(self._user_manager.user, quiz)
        self._quiz_data_manager.add_private_quiz(user_quiz)
        self._reset_question_buffer()
        pass

    def play_quiz(self, quiz):
        def play():
            for question in quiz.questions:
                self._user_manager.user.increase_num_answered_questions()
                print(question.question_txt)
                solution = 0
                try:
                    if type(question) == QUESTION_TYPES['choice']:
                        for index, choice in enumerate(question.choices):
                            print(f'{index}. {choice}')
                        solution = int(input("enter solution: "))
                    elif type(question) == QUESTION_TYPES['number']:
                        solution = int(input("enter solution: "))
                    elif type(question) == QUESTION_TYPES['text']:
                        solution = input("enter solution: ")
                except Exception:
                    raise Exception('Wrong input!')

                if question.answer(solution):
                    print('Right\n')
                    self._user_manager.user.increase_num_correct_answered_questions()
                else:
                    print('Wrong\n')
            self._user_manager.user.increase_num_played_quiz()
            pass

        return play

    def create_public_quiz(self, title):
        quiz = Quiz(title, questions=self._question_buffer)
        self._quiz_data_manager.add_public_quiz(quiz)
        self._reset_question_buffer()
        pass

    def load_public_games(self) -> None:
        """
        loads all public quiz
        :return: None
        """
        return self._quiz_data_manager.get_all_public_quiz()

    def load_private_games(self) -> None:
        """
        loads all private quiz of the current user
        :return: None
        """
        return self._quiz_data_manager.get_all_private_quiz(self._user_manager.user.name)

    def create_question(self, **kwargs) -> None:
        """
        create a new question and add tp question buffer
        :param kwargs: can contain {'question_txt': str, choices': [str, ..., str], 'solution': int}
        :return: None
        """
        question = self._question_factory.make(**kwargs)
        self._question_buffer.append(question)
        pass

    def get_question_buffer_len(self) -> int:
        """
        :return: the len of question buffer
        """
        return len(self._question_buffer)

    def _reset_question_buffer(self) -> None:
        """
        resets the question buffer to []. this is needed after the creation of a new quiz
        :return: None
        """
        self._question_buffer = []
        pass
