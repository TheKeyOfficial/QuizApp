from .question import QuestionFactory, ChoiceQuestion, NumberQuestion, TextQuestion
from .quiz import Quiz
from .question import QuestionFactory
from .quiz_data_manager import QuizDataManager

QUESTION_TYPES = {'choice': ChoiceQuestion, 'number': NumberQuestion, 'text': TextQuestion}

__all__ = ["QuizDataManager", "Quiz", "QuestionFactory", "QUESTION_TYPES"]
