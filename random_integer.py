import random

class RandomInteger:
    @classmethod
    def INPUT_TYPES(cls):
        return {}  # No inputs

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("random_int",)
    FUNCTION = "get_random_integer"
    CATEGORY = "bonkynodes"

    def get_random_integer(self):
        return (random.randint(0, 10000),)  # Returns a random integer between 0 and 10000 (inclusive)