from model.user import RegisteredUser
from model.quiz.quiz import Quiz


class UserQuiz(object):
    def __init__(self, user: RegisteredUser, quiz: Quiz):
        self.user = user
        self.quiz = quiz
        pass
