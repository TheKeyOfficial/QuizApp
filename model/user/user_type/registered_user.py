from ..user import User


class RegisteredUser(User):
    def __init__(self, name: str, password: str, num_played_quiz=0, num_played_questions=0,
                 num_correct_answered_questions=0):
        """
        adds name and user to User
        :param name: primary key to identify a user
        :param password: hashed string containing the password
        """
        super().__init__(num_played_quiz, num_played_questions, num_correct_answered_questions)
        self.name = name
        self.password = password
        pass

    def __dict__(self):
        """
        :return: class object converted to dict
        """
        return_val = {
            self.name:
                {
                    'password': self.password,
                    'num_played_quiz': self.num_played_quiz,
                    'num_played_questions': self.num_played_questions,
                    'num_correct_answered_questions': self.num_correct_answered_questions
                }
        }
        return return_val

    def __str__(self):
        return f'RegisteredUser: {self.name}'

    def __repr__(self):
        return self.__dict__()
