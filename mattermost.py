from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
import requests

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

    def set_status(self, status, emoji, expires_at=None):
        data = {
            "emoji": emoji,
            "text": status,
            "expires_at": expires_at,
        }
        response = requests.put(self.url, headers=self.headers, json=data)
        if response.status_code != 200:
            print(f"Failed to set Mattermost status: {response.content}")
            raise Exception(f"Failed to set Mattermost status: {response.content}")

    def set_now_playing(self, track, artist, duration):
        expires_at = (datetime.now(timezone.utc) + timedelta(seconds=duration)).astimezone()
        status = f"{track} - {artist}"
        print(f"Setting Mattermost status to {status} until {expires_at}")
        self.set_status(status, "headphones", expires_at.isoformat())


    def get_status(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code != 200:
            print(f"Failed to get Mattermost status: {response.content}")
            raise Exception(f"Failed to get Mattermost status: {response.content}")
        return response.json()
