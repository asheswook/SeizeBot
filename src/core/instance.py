from typing import Dict
from src.utils.logger import logger
from src.executors.make import Make
from src.core.ytvideo import YTVideo
from src.utils.database import Database
import datetime as dt


class MVInstance(YTVideo):
    def __init__(self, dict: Dict, db: Database):
        super().__init__(dict["yturl"], dict["var_name"])

        self.album_name = dict["album_name"]
        self.img_url = dict["img_url"]
        self.db = db

    def get_db_view(self) -> int:
        try:
            sql = f"SELECT * FROM data WHERE name = '{self.var_name}'"
            self.db.execute(sql)
            result = self.db.fetch()

            result = result[0][2]  # get viewcount row

        except IndexError:
            logger.warning("It seems to have no result for %s. Create it" %
                           self.var_name)
            sql = f"INSERT INTO data (date, name, viewcount) VALUES ('0', '{self.var_name}', 0)"
            self.db.execute(sql)
            result = 0
            pass

        return result

    def get_view_increase(self) -> str:
        return self.format(super().get_view_int() - self.get_db_view())

    def update_db(self):
        date = str(dt.datetime.now())
        sql = f"UPDATE data SET date='{date}', viewcount={super().get_view_str()} WHERE name='{self.var_name}'"
        self.db.execute(sql)

    def get_dict(self) -> Dict:
        """result = {
            "var_name": var_name
            "album_name": album_name
            "image_url": image_url
            "viewcount": viewcount
            "viewcount_increase": viewcount_increase
        }
        """
        dict = super().get_information()

        dict["album_name"] = self.album_name
        dict["image_url"] = self.img_url
        dict["viewcount_increase"] = self.get_view_increase()
        self.update_db()

        return dict
