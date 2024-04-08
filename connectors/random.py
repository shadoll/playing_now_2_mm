from faker import Faker
import random
import emoji


class RandomConnector:
    def __init__(self):
        self.__faker = Faker()

    @property
    def text(self) -> str:
        return self.__faker.bs().capitalize()

    @property
    def emoji(self) -> dict:
        emoji_names = list(emoji.get_aliases_unicode_dict())
        single_char_emoji_names = [
            name for name in emoji_names if len(emoji.emojize(name)) == 1
        ]
        emoji_name = random.choice(single_char_emoji_names)
        return {
            "name": emoji_name.replace(":", ""),
            "name_with_colons": emoji_name,
            "icon": emoji.emojize(emoji_name),
        }

    @property
    def duration(self) -> int:
        """Return a random duration between 5 and 60 minutes in seconds"""
        return random.randint(5, 60) * 60

    def get(self) -> dict:
        return {
            name: getattr(self, name)
            for name in dir(self)
            if not name.startswith("_") and not callable(getattr(self, name))
        }
