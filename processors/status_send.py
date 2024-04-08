import os
import time
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from connectors.mattermost import MattermostConnector
from connectors.gitlab import GitlabConnector

load_dotenv()


class StatusSend:
    def __init__(self, destination: str | None = None) -> None:
        self.destination: str | None = destination
        self.connector: MattermostConnector | GitlabConnector | None = self.get_connector()

    def get_connector(self) -> MattermostConnector | GitlabConnector | None:
        if self.destination == "mattermost":
            conf = {
                "url": os.getenv("MATTERMOST_SERVER_URL"),
                "token": os.getenv("MATTERMOST_ACCESS_TOKEN"),
            }
            return MattermostConnector(conf)
        elif self.destination == "gitlab":
            conf = {
                "url": os.getenv("GITLAB_SERVER_URL"),
                "token": os.getenv("GITLAB_ACCESS_TOKEN"),
            }
            return GitlabConnector(conf)
        else:
            print("Invalid source")
            return None

    def set_status(self, text, emoji, duration=None, **kwargs):
        if self.connector:
            if duration is not None:
                expires_at = datetime.now(timezone.utc) + timedelta(seconds=duration)
            if isinstance(emoji, dict):
                emoji_name = emoji.get("name")
            else:
                emoji_name = emoji
            data = {
                "emoji": emoji_name,
                "text": text,
                "expires_at": expires_at.isoformat() if expires_at else None,
            }
            now = time.strftime("%H:%M:%S", time.localtime())
            print(f"{now} Setting status to {self.destination.capitalize()} of {emoji.get("icon")} {text} ⏱️ for {duration} seconds")
            try:
                self.connector.send(data=data)
            except Exception as e:
                print(e)

    def clear_status(self):
        if self.connector:
            try:
                self.connector.send(data={"emoji": "", "text": "", "expires_at": ""})
            except Exception as e:
                print(e)
