from ..interfaces import MenuInterface


class PlayMenu(MenuInterface):
    PUBLIC_QUIZ = 'Public'
    PRIVATE_QUIZ = 'Private'

    def __init__(self):
        super().__init__(title='\nPLAY QUIZ\n')
        self.USER_MENU = {self.PUBLIC_QUIZ: self.play_public,
                          self.EXIT: self.quit}
        self.REGISTERED_USER_MENU = {self.PUBLIC_QUIZ: self.play_public,
                                     self.PRIVATE_QUIZ: self.play_private,
                                     self.EXIT: self.quit}
        self.active_menu = self.USER_MENU
        self.show()
        pass

    def play_public(self):
        games = self.game_manager.load_public_games()
        self.set_available_games_as_active_menu(games)
        pass

    def play_private(self):
        games = self.game_manager.load_private_games()
        self.set_available_games_as_active_menu(games)
        pass

    def set_available_games_as_active_menu(self, games):
        self.active_menu = {self.EXIT: self.quit}
        if games is not None:
            for quiz_title, quiz in games.items():
                self.active_menu.update({quiz_title: self.game_manager.play_quiz(quiz)})
            self.clear_menu()
            self.build_menu_items()
            print(self.contend)
            selection = self.get_choice_input(self.option_range)
            self.select_menu_item(selection)

        pass

    def build_menu(self):
        self.clear_menu()
        if self.user_manager.is_registered_user():
            self.active_menu = self.REGISTERED_USER_MENU
        else:
            self.active_menu = self.USER_MENU
        self.build_menu_items()
        pass
