from multiprocessing.dummy import Pool, Process
from src.utils.logger import logger
from src.executors.take_screenshot import take_screen
from src.executors.make import Make
from src.executors.twicenest import Twicenest
from src.executors.want import Want
from src.utils.database import Database
from src.core.instance import MVInstance
import time
import multiprocessing

time.sleep(5)
db = Database()

mv_list = [
    {
        "var_name": "FOL",
        "album_name": "Formula of Love",
        "yturl": "https://www.youtube.com/watch?v=vPwaXytZcgI",
        "img_url": "https://upload.wikimedia.org/wikipedia/en/8/8e/Twice_-_Formula_of_Love.png"
    },
    {
        "var_name": "TOL",
        "album_name": "Taste of Love",
        "yturl": "https://www.youtube.com/watch?v=XA2YEHn-A8Q",
        "img_url": "https://upload.wikimedia.org/wikipedia/en/8/87/Twice_-_Taste_of_Love_(EP).png"
    }
]


def doWork():
    logger.info("doWork")
    db.ping()

    make = Make()

    twicenest = Twicenest()
    want = Want()
    twicenest.change_option("테스트", "개발 버전 테스트 중입니다.")
    want.change_option("테스트", "개발 버전 테스트 중입니다.")

    height = 100

    for mv in mv_list:
        instance = MVInstance(mv, db)
        make.add_mv_dict(instance.get_dict())
        height += 200

    make.make_html()
    take_screen(height)

    twicenest.POST()
    want.POST()


doWork()
