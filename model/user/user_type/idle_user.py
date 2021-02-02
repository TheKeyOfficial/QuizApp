from ..user import User


class IdleUser(User):
    def __init__(self):
        """
        creates a empty user object
        num_played_quiz = 0
        num_played_questions = 0
        num_correct_answered_questions = 0
        """
        super().__init__(0, 0, 0)
        pass
