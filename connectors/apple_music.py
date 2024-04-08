from appscript import app  # type: ignore


class AppleMusic:
    def __init__(self):
        self.__music_app = app("Music")
        self.__current_track = None
        self.__player_position = None
        self.get_current_track_info()

    @property
    def text(self) -> str:
        return f"{self.name} - {self.artist}"

    @property
    def emoji(self) -> dict:
        return {
            "name": "headphones",
            "name_with_colons": ":headphones:",
            "icon": "🎧",
        }

    @property
    def name(self) -> str:
        if self.__current_track is not None:
            return str(self.__current_track.name.get())
        return ""

    @property
    def artist(self) -> str:
        if self.__current_track is not None:
            return str(self.__current_track.artist.get())
        return ""

    @property
    def album(self) -> str:
        if self.__current_track is not None:
            return str(self.__current_track.album.get())
        return ""

    @property
    def duration(self) -> int:
        if self.__current_track is not None:
            return int(self.__current_track.duration.get())
        return 0

    @property
    def elapsed_time(self) -> float:
        if self.__player_position is not None:
            return self.__player_position
        return 0

    @property
    def remaining_time(self) -> float:
        return self.duration - self.elapsed_time

    def get_current_track_info(self):
        try:
            self.__current_track = self.__music_app.current_track.get()
            self.__player_position = self.__music_app.player_position.get()
        except Exception as e:
            print(f"Failed to get current track info: {e}")

    def get(self) -> dict:
        return {
            name: getattr(self, name)
            for name in dir(self)
            if not name.startswith("_") and not callable(getattr(self, name))
        }
