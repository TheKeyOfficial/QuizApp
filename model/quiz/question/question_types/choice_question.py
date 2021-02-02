from .question import Question


class ChoiceQuestion(Question):
    def __init__(self, question_txt: str, choices: list, solution: int):
        super().__init__(question_txt)
        if type(choices) is list and 2 <= len(choices) <= 4:
            self.choices = choices
        else:
            raise Exception('A Choice Question must have more than 2 and less than 4 options')
        if type(solution) is int:
            self.solution = solution
        else:
            raise Exception('The solution must be a number ')
        pass

    def answer(self, solution: int) -> bool:
        if type(solution) is int:
            if self.solution == solution:
                return True
        else:
            raise ValueError
        pass

    def __repr__(self):
        return self.__dict__()

    def __str__(self):
        txt = str
        txt += self.question_txt + '\n'
        for i, choice in enumerate(self.choices):
            txt += f'{i}. {choice} + \n'
        return txt

    def __dict__(self):
        return_val = {
            'question_txt': self.question_txt,
            'choices': self.choices,
            'solution': self.solution
        }
        return return_val




