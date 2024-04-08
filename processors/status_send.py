import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from connectors.mattermost import MattermostConnector

load_dotenv()


class StatusSend:
    def __init__(self):
        conf = {
            "url": os.getenv("MATTERMOST_SERVER_URL"),
            "token": os.getenv("MATTERMOST_ACCESS_TOKEN"),
        }
        self.connector = MattermostConnector(conf)

    def set_status(self, text, emoji, duration=None, **kwargs):
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
        try:
            self.connector.send(data=data)
        except Exception as e:
            print(e)

    def clear_status(self):
        try:
            self.connector.send(data={"emoji": "", "text": "", "expires_at": ""})
        except Exception as e:
            print(e)
