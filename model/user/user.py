class User(object):
    def __init__(self, num_played_quiz, num_played_questions, num_correct_answered_questions):
        """
        user object
        :param num_played_quiz: numbers of played quiz
        :param num_played_questions: numbers of played questions
        :param num_correct_answered_questions: numbers of correct answered questions
        """
        # init parameters
        self.num_played_quiz = num_played_quiz
        self.num_played_questions = num_played_questions
        self.num_correct_answered_questions = num_correct_answered_questions
        pass

    def get_average_correctly_answered(self) -> float:
        """
        :return: percentage evaluation of correctly answered questions
        """
        # check if the user ever played a game
        if self.num_played_questions > 0:
            return round((self.num_correct_answered_questions / self.num_played_questions) * 100, 1)
        return 0

    def increase_num_played_quiz(self) -> None:
        """
        increases the num of played quiz by 1
        :return: None
        """
        self.num_played_quiz += 1
        pass

    def increase_num_answered_questions(self) -> None:
        """
        increases the num of answered questions by 1
        :return: None
        """
        self.num_played_questions += 1
        pass

    def increase_num_correct_answered_questions(self) -> None:
        """
        increases the num of correct answered questions by 1
        :return: None
        """
        self.num_correct_answered_questions += 1
        pass

    def __dict__(self):
        return_val = {
            'num_played_quiz': self.num_played_quiz,
            'num_played_questions': self.num_played_questions,
            'num_correct_answered_questions': self.num_correct_answered_questions
        }
        return return_val
