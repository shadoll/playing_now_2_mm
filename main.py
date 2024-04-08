from dotenv import load_dotenv
from processors.status_send import StatusSend
from processors.music import MusicProcessor
from processors.text import TextProcessor
import argparse
import time
import os

load_dotenv()

SLEEP_TIME = 3


def get_status(source: str | None = None) -> dict:
    if source == "random":
        return TextProcessor(source=source).get_status()
    if source in ["spotify", "apple_music", "autodetect"]:
        track = MusicProcessor(source=source).get_status()
        return track
    return {}


def send_user_status(destination: str |None = None, status = {}) -> bool:
    try:
        StatusSend(destination=destination).set_status(**status)
        return True
    except Exception as e:
        print(e)
        return False


def main(source: str = "autodetect", destination: str = "mattermost"):
    status_curr = {"status": None}
    while True:
        status = get_status(source)
        if status.get("text", "") != status_curr.get("text", ""):
            status_result = send_user_status(destination=destination, status=status)
            status_curr = status
            if not status_result:
                continue
        time.sleep(status.get("duration") or SLEEP_TIME)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Source can be "env", "autodetect", "spotify", "apple_music", "random"
    parser.add_argument("--source", help="source to use for connector", default="env")
    # Destination can be "env", "mattermost", "gitlab"
    parser.add_argument(
        "--destination", help="destination to use for connector", default="env"
    )
    args = parser.parse_args()
    if args.source == "env":
        args.source = os.getenv("SOURCE", "autodetect")
    if args.destination == "env":
        args.destination = os.getenv("DESTINATION", "mattermost")
    main(args.source, args.destination)
