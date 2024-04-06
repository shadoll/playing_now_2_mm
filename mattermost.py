from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
import requests
import emoji

load_dotenv()


class Mattermost:
    def __init__(self, user_id="me"):
        host = os.getenv("MATTERMOST_SERVER_URL", "http://localhost")
        access_token = os.getenv("MATTERMOST_ACCESS_TOKEN", "")
        self.user_id = user_id
        self.url = f"{host}/api/v4/users/{self.user_id}/status/custom"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def set_status(self, status, emoji_name, expires_at=None):
        emoji_icon = emoji.emojize(f":{emoji_name}:", language="alias")
        print(f"Setting Mattermost status to {emoji_icon} {status} until {expires_at}")
        data = {
            "emoji": emoji_name,
            "text": status,
            "expires_at": expires_at.isoformat() if expires_at else None,
        }
        response = requests.put(self.url, headers=self.headers, json=data)
        if response.status_code != 200:
            print(f"Failed to set Mattermost status: {response.content}")
            raise Exception(f"Failed to set Mattermost status: {response.content}")

    def clear_status(self):
        self.set_status("", "", None)

    def set_now_playing(self, track, artist, duration):
        expires_at = (
            datetime.now(timezone.utc) + timedelta(seconds=duration)
        ).astimezone()
        status = f"{track} - {artist}"
        self.set_status(status, "headphones", expires_at)

    def get_status(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code != 200:
            print(f"Failed to get Mattermost status: {response.content}")
            raise Exception(f"Failed to get Mattermost status: {response.content}")
        return response.json()
