from connectors.random import RandomConnector


class TextProcessor:
    def __init__(self, source: str | None = None):
        self.source: str | None = source
        self.connector: RandomConnector | None = self.get_connector()

    def get_connector(self) -> RandomConnector | None:
        if self.source == "random":
            return RandomConnector()
        else:
            print("Invalid source")
            return None

    def get_status(self) -> dict:
        if self.connector:
            return self.connector.get()
        return {}
