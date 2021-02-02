from .face_interface import FaceInterface


class MenuInterface(FaceInterface):
    EXIT = 'Exit'

    def __init__(self, title: str):
        super().__init__(title)

        self.active_menu = dict()
        self.contend = ''
        self.option_range = 0
        pass

    def show(self):
        """
        display menu to select available quiz games.
        :return: None
        """
        # create dynamic menu and print it
        self.build_menu()
        print(self.contend)
        # wait for user input
        selection = self.get_choice_input(self.option_range)
        # execute the selection
        self.select_menu_item(selection)
        pass

    def build_menu(self):
        self.clear_menu()
        self.build_menu_items()
        pass

    def build_menu_items(self) -> None:
        """
        number the menu items and add them to the content.
        This allows a selection by entering a number for the user
        :return: None
        """
        self.option_range = len(self.active_menu)
        self.contend = self.TITLE
        for index, menu_item in enumerate(self.active_menu.keys()):
            if index == self.option_range:
                self._add_contend(index, menu_item, new_line=False)
            self._add_contend(index, menu_item)

    def _add_contend(self, index: int, text: str, new_line=True) -> None:
        """
        add item to  content
        :param index: index with which the menu object can be selected
        :param text: text of the menu object
        :return: None
        """
        self.contend += f'{index}. {text}'
        if new_line:
            self.contend += '\n'
        pass

    def select_menu_item(self, selection):
        """

        :param selection:
        :return:
        """
        # select runnable object from active menu dict bei index.
        runnable_object = list(self.active_menu.values())[selection]
        # run selected object
        runnable_object()
        pass

    def clear_menu(self):
        self.contend = ''
        self.option_range = 0
        pass

    def quit(self) -> None:
        """
        terminates the menu by not starting a new process and returning to the MainLoop.
        :return: None
        """
        pass
