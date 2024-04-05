from datetime import datetime
import time
from music import Music
from mattermost import Mattermost
from connectors.apple_music import AppleMusic
from connectors.spotify import Spotify
from dotenv import load_dotenv
import os

load_dotenv()

SLEEP_TIME = 3
MUSIC_APP = (
    os.getenv("MUSIC_APP", "apple_music").replace("_", " ").title().replace(" ", "")
)


def playing_now() -> tuple:
    music = Music(connector=globals()[MUSIC_APP])
    return music.get_current_track_info()


def set_now_playing(name, artist, duration):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"{now} 🎧 {name} - {artist} ⏲️ {duration}")
    if name and artist and duration:
        Mattermost().set_now_playing(name, artist, duration)


def main():
    name_curr, artist_curr, duration_curr = playing_now()
    set_now_playing(name_curr, artist_curr, duration_curr)

    while True:
        name, artist, duration = playing_now()
        if name != name_curr:
            set_now_playing(name, artist, duration)
            name_curr = name
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
