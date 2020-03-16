import sys_logging


class Song:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        sys_logging.info(f"I'm listening to {self.title}")

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title.upper()

    title = property(get_title, set_title)


class AnotherSong:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        sys_logging.info(f"I'm listening to {self.title}")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title.upper()


Teddy_Bear = AnotherSong('Teddy Bear')
Teddy_Bear.show_title()
