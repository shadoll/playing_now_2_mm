import subprocess
from connectors.apple_music import AppleMusic
from connectors.spotify import Spotify


class MusicProcessor:
    def __init__(self, source: str | None = None):
        self.source: str | None = source
        self.connector: Spotify | AppleMusic | None = self.get_connector()

    def get_connector(self) -> Spotify | AppleMusic | None:
        if self.source == "autodetect":
            self.source = self.get_current_music_player()

        match self.source:
            case "spotify":
                return Spotify()
            case "apple_music":
                return AppleMusic()
            case _:
                print("Active music player not found")
                return None

    def get_status(self) -> dict:
        if self.connector:
            return self.connector.get()
        return {}

    @staticmethod
    def get_current_music_player():
        spotify_status = (
            subprocess.check_output(
                "osascript -e 'application \"Spotify\" is running'", shell=True
            )
            .decode()
            .strip()
        )
        apple_music_status = (
            subprocess.check_output(
                "osascript -e 'application \"Music\" is running'", shell=True
            )
            .decode()
            .strip()
        )
        if spotify_status == "true":
            player = "spotify"
        elif apple_music_status == "true":
            player = "apple_music"
        else:
            player = None
        return player
