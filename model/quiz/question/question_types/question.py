from abc import ABC, abstractmethod


class Question(ABC):
    def __init__(self, question_txt: str):
        if type(question_txt) is str and not '' or None:
            self.question_txt = question_txt
        else:
            raise ValueError
        pass

    @abstractmethod
    def answer(self, solution):
        raise NotImplementedError

    @abstractmethod
    def __dict__(self):
        raise NotImplementedError
