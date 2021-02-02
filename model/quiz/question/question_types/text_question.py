from .question import Question


class TextQuestion(Question):
    def __init__(self, question_txt: str, solution: str):
        super().__init__(question_txt)
        if type(solution) is str:
            self.solution = solution
        else:
            raise Exception('The solution must be a string')
        pass

    def answer(self, solution: str) -> bool:
        if type(solution) is str:
            if self.solution == solution:
                return True
        else:
            raise ValueError
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.question_txt + '\n'

    def __dict__(self):
        return_val = {
            'question_txt': self.question_txt,
            'solution': self.solution
        }
        return return_val
