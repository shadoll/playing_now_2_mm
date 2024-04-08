import requests

class MattermostConnector:
    def __init__(self, connection_config) -> None:
        self.url = connection_config.get("url", "https://mattermost.com")
        self.token = connection_config.get("token", "")
        self.connect(connection_config.get("user_id", "me"))

    def connect(self, user_id):
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        self.url = f"{self.url}/api/v4/users/{user_id}/status/custom"

    def send(self, data):
        response = requests.put(self.url, headers=self.headers, json=data)
        if response.status_code != 200:
            raise Exception(f"Failed to set Mattermost status: {response.content!r}")
