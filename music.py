from mattermost import Mattermost

class Music:
    def __init__(self, connector):
        self.mattermost = Mattermost()
        self.connector = connector()

    def get_current_track_info(self) -> tuple:
        return self.connector.get_current_track_info()
