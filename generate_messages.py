replies = [
    "You're looking absolutely gorgeous today ;)",
    "Here's a bonus hug from me!",
    "Go drink some water!",
    "I love your tweets!",
    "You're awesome",
    "Should I be worried that my creator is not cool as you?",
    "You're are so smart, people had to increase range of the IQ scale",
    "I want to be as cool as you",
    "Do you want to go out on a coffee date maybe?",
]


def generate_funny_reply(tweet_text):
    # TODO: modify this so we generate funny reply based on tweet text
    return replies[random.randrange(0, 8)]
