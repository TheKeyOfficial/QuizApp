from abc import ABC, abstractmethod
from ..exeptions import InvalidInput
from control import UserManager, GameManager


class FaceInterface(ABC):
    CHOICE_INPUT = 'Select: '

    def __init__(self, title: str):
        self.TITLE = title
        self.user_manager = UserManager.instance()
        self.game_manager = GameManager.instance()
        pass

    @abstractmethod
    def show(self):
        """
        display a user interface
        :return: None
        """
        raise NotImplementedError

    def get_choice_input(self, input_range: int):
        """
        function which returns the choice selection of the user
        :param input_range: int which defines the max possible input
        :return: a int which represents the input
        """
        try:
            selection = int(input(self.CHOICE_INPUT))
            if selection in range(0, input_range):
                return selection
            else:
                raise InvalidInput
        except Exception:
            raise InvalidInput
