from faker import Faker
import random
import emoji


class Random:
    def __init__(self):
        self.faker = Faker()

    def get_random_activity(self) -> tuple:
        activity = self.faker.bs().capitalize()  # Generate a random activity
        emoji = self.get_random_emoji_name()  # Get a random emoji
        duration = random.randint(5, 60)  # Duration in minutes
        return activity, emoji, duration

    def get_random_emoji_name(self) -> str:
        emoji_names = list(emoji.get_aliases_unicode_dict())
        single_char_emoji_names = [
            name for name in emoji_names if len(emoji.emojize(name)) == 1
        ]
        random_emoji_name = random.choice(single_char_emoji_names)
        return random_emoji_name

    def get_random_emoji(self) -> str:
        random_emoji = emoji.emojize(self.get_random_emoji_name())

        return random_emoji
