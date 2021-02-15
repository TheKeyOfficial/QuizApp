from ..interfaces import DataManagerInterface
from .quiz import Quiz
from .question import QuestionFactory
from desing_pattern import Singleton


@Singleton
class QuizDataManager(DataManagerInterface):
    LOGIN_DATA = 'login_data'
    QUIZ_DATA = 'quiz_data'
    PRIVATE = 'private'
    PUBLIC = 'public'

    def __init__(self):
        super().__init__()
        self.question_factory = QuestionFactory()
        pass

    def add_public_quiz(self, quiz: Quiz):
        data = self.database_manager.read_database()
        reg_user_dict = quiz.__dict__()
        try:
            data[self.QUIZ_DATA][self.PUBLIC].update(reg_user_dict)
        except Exception:
            try:
                data.update({self.QUIZ_DATA: {self.PUBLIC: reg_user_dict,
                                              self.PRIVATE: data[self.QUIZ_DATA][self.PRIVATE]}})
            except Exception:
                data.update({self.QUIZ_DATA: {self.PUBLIC: reg_user_dict,
                                              self.PRIVATE: {}}})
        self.database_manager.write_database(data)
        pass

    def add_private_quiz(self, user_quiz):
        data = self.database_manager.read_database()
        user_name = user_quiz.user.name
        quiz = user_quiz.quiz.__dict__()
        try:
            data[self.QUIZ_DATA][self.PRIVATE][user_name].update(quiz)
        except Exception:
            try:
                data.update({self.QUIZ_DATA: {self.PRIVATE: {user_name: quiz},
                                              self.PUBLIC: data[self.QUIZ_DATA][self.PUBLIC]}})
            except Exception:
                data.update({self.QUIZ_DATA: {self.PRIVATE: {user_name: quiz},
                                              self.PUBLIC: {}}})
        self.database_manager.write_database(data)
        pass

    def get_all_public_quiz(self) -> dict:
        try:
            data = self.database_manager.read_database()[self.QUIZ_DATA][self.PUBLIC]
            return self._create_quiz_dict(data)
        except KeyError:
            print('No public quiz exists')
        pass

    def get_all_private_quiz(self, username: str) -> dict:
        try:
            data = self.database_manager.read_database()[self.QUIZ_DATA][self.PRIVATE][username]
            return self._create_quiz_dict(data)
        except KeyError:
            print('No private quiz exists')
        pass

    def _create_quiz_dict(self, data) -> dict:
        quiz_list = {}
        for quiz_title, questions in data.items():
            quiz_questions = []
            for question_kwargs in questions['questions']:
                quiz_questions.append(self.question_factory.make(**question_kwargs))
            quiz_list.update({quiz_title: Quiz(quiz_title, quiz_questions)})
        return quiz_list
