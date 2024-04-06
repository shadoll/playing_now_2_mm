from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from mattermost import Mattermost
from processors.music import MusicProcessor
from processors.text import TextProcessor
import argparse
import time

load_dotenv()

SLEEP_TIME = 3


def get_status(source: str | None = None) -> dict:
    if source == "random":
        activity, emoji, duration = TextProcessor(source=source).get_satus()
        return {
            "status": activity,
            "emoji": emoji.replace(":", ""),
            "expires_at": datetime.now(timezone.utc) + timedelta(minutes=duration),
            "ending_time": duration * 60,
        }
    if source == "music":
        track, artist, duration, elapsed_time = (
            MusicProcessor().get_current_track_info()
        )
        if track and artist and duration:
            now = datetime.now(timezone.utc)
            print(f"{now} 🎧 {track} - {artist}")
            expires_at = (
                now + timedelta(seconds=duration) - timedelta(seconds=elapsed_time)
            ).astimezone()
            return {
                "status": f"{track} - {artist}",
                "emoji": "headphones",
                "expires_at": expires_at,
                "ending_time": duration - elapsed_time,
            }
    return {
        "status": None,
        "emoji": None,
        "expires_at": None,
        "ending_time": None,
    }


def send_user_status(status, emoji, expires_at=None, **kwargs):
    Mattermost().set_status(status, emoji, expires_at=expires_at)


def main(source: str | None = "music"):
    status_curr = {"status": None}
    while True:
        status = get_status(source)
        if status.get("status") != status_curr.get("status"):
            send_user_status(**status)
            status_curr = status
        time.sleep(status.get("ending_time") or SLEEP_TIME)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", help="source to use for connector", default="music")
    args = parser.parse_args()
    main(args.source)
