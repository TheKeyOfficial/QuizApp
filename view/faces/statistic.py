from view.interfaces.face_interface import *


class Statistic(FaceInterface):

    def __init__(self, title='STATISTICS'):
        super().__init__(title=title)
        self.show()
        pass

    def show(self):
        print(self.TITLE)
        print(f'Played quiz: {self.user_manager.user.num_played_quiz}')
        print(f'Answered questions: {self.user_manager.user.num_played_questions}')
        print(f'Average of correctly answered questions: {self.user_manager.user.get_average_correctly_answered()}%')
        pass
