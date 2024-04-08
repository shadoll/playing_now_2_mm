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


def send_user_status(**kwargs) -> bool:
    try:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(
            f"{now} Setting Mattermost status to {kwargs.get('emoji',{}).get('icon','')} {kwargs.get('text')} ⏱️ for {kwargs.get('duration')} seconds"
        )
        StatusSend().set_status(**kwargs)
        return True
    except Exception as e:
        print(e)
        return False


def main(source: str = "autodetect"):
    status_curr = {"status": None}
    while True:
        status = get_status(source)
        if status.get("text", "") != status_curr.get("text", ""):
            status_result = send_user_status(**status)
            status_curr = status
            if not status_result:
                continue
        time.sleep(status.get("duration") or SLEEP_TIME)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Source can be "autodetect", "spotify", "apple_music", "random"
    parser.add_argument(
        "--source", help="source to use for connector", default="autodetect"
    )
    args = parser.parse_args()
    if args.source == "env":
        args.source = os.getenv("SOURCE", "autodetect")
    main(args.source)
