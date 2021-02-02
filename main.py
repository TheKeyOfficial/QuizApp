from view import ViewManager
from model import QuizDataManager


if __name__ == '__main__':
    # view_manager = ViewManager()
    # view_manager.mainloop()

    quiz_manager = QuizDataManager()
    quiz_manager.add_private_quiz()
    quiz_manager.add_public_quiz()

