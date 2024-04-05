import subprocess
from connectors.apple_music import AppleMusic
from connectors.spotify import Spotify
import os
from dotenv import load_dotenv

class Music:
    def __init__(self):
        load_dotenv()
        self.music_app = os.getenv('MUSIC_APP', 'autodetect')
        if self.music_app == 'autodetect':
            self.music_app = self.get_current_music_player()
        self.connector = self.get_connector()

    def get_connector(self):
        if self.music_app == 'spotify':
            return Spotify()
        elif self.music_app == 'apple_music':
            return AppleMusic()
        else:
            raise ValueError(f'Invalid music app: {self.music_app}')

    def get_current_track_info(self) -> tuple:
        if self.connector:
            return self.connector.get_current_track_info()
        return None, None, None

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
            player = "Spotify"
        elif apple_music_status == "true":
            player = "Apple Music"
        else:
            player = None

        # print(f"Detected 📀 player: {player}")
        return player
