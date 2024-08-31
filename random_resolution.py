import random
import comfy.samplers

class RandomResolution:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolutions": ("STRING", {"multiline": True}),
                "seed": ("INT",{"default": random.randint(1,999999999), "min": 0, "max": 0xffffffffffffffff})
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_random_resolution"
    CATEGORY = "bonkynodes"

    def get_random_resolution(self, resolutions, seed): 
        res_list = resolutions.split(",")
        chosen_res = random.choice(res_list)
        width, height = map(int, chosen_res.split("x"))
        return (width, height)