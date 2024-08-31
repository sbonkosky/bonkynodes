import random
import comfy.samplers

class RandomStuff:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolutions": ("STRING", {"multiline": True, "default": "1024x1024,1920x1080,1080x1920"}),
                "samplers": ("STRING", {"multiline": True, "default": "euler|normal,euler|simple,euler|beta,deis|normal,deis|simple,deis|bdim_uniform,uni_pc_bh2|beta,heun|normal"}),
                "seed": ("INT",{"default": random.randint(1,999999999), "min": 0, "max": 0xffffffffffffffff})
            }
        }

    RETURN_TYPES = ("INT", "INT", "STRING", "STRING")
    RETURN_NAMES = ("width", "height", "sampler", "scheduler")
    FUNCTION = "get_random_stuff"
    CATEGORY = "bonkynodes"

    def get_random_stuff(self, resolutions, samplers, seed): 
        res_list = resolutions.split(",")
        chosen_res = random.choice(res_list)
        width, height = map(int, chosen_res.split("x"))

        sampler_list = samplers.split(",")
        chosen_sampler_pair = random.choice(sampler_list)
        sampler, scheduler = chosen_sampler_pair.split("|")

        return (width, height, sampler, scheduler) 