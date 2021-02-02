from .faces import MainMenu


class ViewManager(object):
    def __init__(self):
        self._run = True
        pass

    def mainloop(self):
        """
        starts the main menu and displayed in a loop
        :return:
        """
        while self._run:
            try:
                MainMenu().show()
            except Exception as e:
                print(e)
        pass

    def stop_mainloop(self) -> None:
        """
        set the run variable to False and stops the mainloop
        :return: None
        """
        self._run = False
        pass
