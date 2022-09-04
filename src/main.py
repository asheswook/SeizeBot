from multiprocessing.dummy import Pool, Process
from src.core.process import MyProcess
from src.utils.logger import logger
from src.executors.take_screenshot import take_screen
from src.executors.make import Make
from src.executors.twicenest import Twicenest
from src.executors.want import Want
from src.executors.dcinside import Dcinside
from src.utils.database import Database
from src.core.instance import MVInstance
import time
import multiprocessing

time.sleep(5)
db = Database()

mv_list = [
    {
        "var_name": "TTT",
        "album_name": "Talk that Talk",
        "yturl": "https://www.youtube.com/watch?v=k6jqx9kZgPM",
        "img_url": "https://upload.wikimedia.org/wikipedia/en/6/67/Twice_-_Between_1%262.png"
    },
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
    dcinside = Dcinside('twiceyou')

    twicenest.change_option("테스트", "개발 버전 테스트 중입니다.")
    want.change_option("테스트", "개발 버전 테스트 중입니다.")
    dcinside.change_option("테스트", "개발 버전 테스트 중입니다.")

    height = 1000

    procs = []

    for mv in mv_list:
        proc = MyProcess(mv, make, db)
        procs.append(proc)
        proc.start()

    for proc in procs:  # wait until all processes done
        proc.join()

    make.make_html()
    take_screen(height)

    twicenest.POST()
    want.POST()
    dcinside.POST()


doWork()
