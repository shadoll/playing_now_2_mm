import requests

class GitlabConnector:
    def __init__(self, connection_config) -> None:
        self.url = connection_config.get("url", "https://gitlab.com")
        self.token = connection_config.get("token", "")
        self.connect()

    def connect(self):
        self.headers = {
            "PRIVATE-TOKEN": f"{self.token}",
            "Content-Type": "application/json",
        }
        self.url = f"{self.url}/api/v4/user/status"

    def send(self, data):
        request_data = {
            "emoji": data["emoji"],
            "message": data["text"],
            "availability": "not_set",
            "clear_status_after": "30_minutes",
        }
        response = requests.patch(self.url, headers=self.headers, json=request_data)
        if response.status_code != 200:
            raise Exception(f"Failed to set GitLab status: {response.content!r}")
