import subprocess
from connectors.apple_music import AppleMusic
from connectors.spotify import Spotify
import os
from dotenv import load_dotenv


class MusicProcessor:
    def __init__(self):
        load_dotenv()
        self.music_app = os.getenv("MUSIC_APP", "autodetect")
        if self.music_app == "autodetect":
            self.music_app = self.get_current_music_player()
        self.connector: Spotify | AppleMusic | None = self.get_connector()

    def get_connector(self) -> Spotify | AppleMusic | None:
        match self.music_app:
            case "spotify":
                return Spotify()
            case "apple_music":
                return AppleMusic()
            case _:
                print("Active music player not found")
                return None

    def get_current_track_info(self) -> tuple:
        if self.connector:
            return self.connector.get_current_track_info()
        return None, None, None, None

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

        # print(f"Detected 📀 player: {player}")
        return player
