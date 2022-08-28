from src.utils.template import Engine, By
from src.utils.logger import logger
from typing import Dict, List

"""
"input" must be dict
input = {
    {
        "var_name": "FOL",
        "album_name": "Folmula of Love",
        "viewcount": "1000000"
        "image_url": "https://i.ytimg.com/vi/Q-_q-_q-_q/hqdefault.jpg"
    }
    {
        "var_name": "TT",
        "album_name": "TT",
        "viewcount": "1000000"
        "image_url": "https://i.ytimg.com/vi/Q-_q-_q-_q/hqdefault.jpg"
    }
}
"""


class Make:
    def __init__(self):
        self.mvs = []

    def add_mv(self, var_name: str, album_name: str, viewcount: str, viewcount_increase: str, image_url: str):
        dict = {
            "var_name": var_name,
            "image_url": image_url,
            "album_name": album_name,
            "viewcount": viewcount,
            "viewcount_increase": viewcount_increase
        }
        self.mvs.append(dict.copy())

    def add_mv_dict(self, mv_dict: Dict):
        """Dict must be:\n
        dict = {
            "var_name": var_name,
            "image_url": image_url,
            "album_name": album_name,
            "viewcount": viewcount,
            "viewcount_increase": viewcount_increase
        }
        """
        self.mvs.append(mv_dict)

    def get_mv_var_name(self) -> list:
        return [mv["var_name"] for mv in self.mvs]

    def make_html(self):
        engine = Engine()

        engine.repeat_add_content(self.get_mv_var_name())
        engine.find_variable()

        for mv in self.mvs:
            engine.replace_variable(
                By.NAME, mv["var_name"] + "0", mv["image_url"])
            engine.replace_variable(
                By.NAME, mv["var_name"] + "1", mv["album_name"])
            engine.replace_variable(
                By.NAME, mv["var_name"] + "2", mv["viewcount"])
            engine.replace_variable(
                By.NAME, mv["var_name"] + "3", mv["viewcount_increase"])
