class Quiz(object):
    title = str
    questions = list

    def __init__(self, title: str, questions: list):
        if type(questions) is list and 3 <= len(questions) <= 10:
            self.title = title
            self.questions = questions
        else:
            raise Exception('A quiz must contain min 3 and max 10 questions!')
        pass

    def __repr__(self):
        return self.__dict__()

    def __dict__(self):
        questions = []
        for question in self.questions:
            questions.append(question.__dict__())
        return_val = {
            self.title:
                {
                    'questions': questions
                }
        }
        return return_val
