import pafy
from src.utils.logger import logger
from src.utils.database import Database as db
import datetime as dt


class YTVideo:
    def __init__(self, url: str, var_name: str):
        self.url = url
        self.var_name = var_name

        logger.info("Load YTVideo: %s" % self.url)
        self.video = pafy.new(self.url)
        logger.info("Successfully load YTVideo: %s" % self.url)

    @staticmethod
    def format(view: int) -> str:
        return str(format(view, ",d"))

    def get_view_int(self) -> int:
        return self.video.viewcount

    def get_view_str(self) -> str:
        return str(self.video.viewcount)

    def get_view_formatted(self) -> str:
        return self.format(self.get_view_int())

    def get_information(self) -> dict:
        return {
            "var_name": self.var_name,
            "viewcount": self.get_view_formatted()
        }
