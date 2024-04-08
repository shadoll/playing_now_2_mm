import osascript  # type: ignore


class Spotify:
    def __init__(self):
        self.__request_prefix = 'tell application "Spotify" to'
        self.__request_current_track = "of current track as string"
        self.name: str = ""
        self.artist: str = ""
        self.album: str = ""
        self.duration: int = 0
        self.elapsed_time: float = 0
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
    def remaining_time(self) -> float:
        return self.duration - self.elapsed_time

    def get_current_track_info(self):
        try:
            name_code = f"{self.__request_prefix} name {self.__request_current_track}"
            artist_code = (
                f"{self.__request_prefix} artist {self.__request_current_track}"
            )
            album_code = f"{self.__request_prefix} album {self.__request_current_track}"
            duration_code = (
                f"{self.__request_prefix} duration {self.__request_current_track}"
            )
            elapsed_time_code = f"{self.__request_prefix} player position as string"

            self.name = osascript.osascript(name_code)[1]
            self.artist = osascript.osascript(artist_code)[1]
            self.album = osascript.osascript(album_code)[1]
            self.duration = round(int(osascript.osascript(duration_code)[1]) / 1000)
            self.elapsed_time = float(
                osascript.osascript(elapsed_time_code)[1].replace(",", ".")
            )
        except Exception as e:
            print(f"Failed to get current track info: {e}")

    def get(self) -> dict:
        return {
            name: getattr(self, name)
            for name in dir(self)
            if not name.startswith("_") and not callable(getattr(self, name))
        }
