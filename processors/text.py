from connectors.random import Random


class TextProcessor:
    def __init__(self, source: str | None = None):
        self.source: str | None = source
        self.connector = self.get_connector()

    def get_connector(self):
        if self.source == "random":
            return Random()
        else:
            raise ValueError("Invalid source")

    def get_satus(self) -> tuple:
        if self.connector:
            return self.connector.get_random_activity()
        return None, None, None
