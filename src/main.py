from multiprocessing.dummy import Pool, Process
from src.executors.dcinside import Dcinside
from src.utils.logger import logger
from src.executors.take_screenshot import take_screen
from src.executors.make import Make
from src.executors.twicenest import Twicenest
from src.executors.want import Want
from src.utils.database import Database
from src.core.instance import MVInstance
import time
import schedule
import json

time.sleep(5)
db = Database()

mv_list_file = open("mv_list.json", encoding='utf-8')
mv_list = json.load(mv_list_file)


def doWork():
    logger.info("Let's work!")
    db.ping()

    make = Make()

    twicenest = Twicenest()
    want = Want()
    dcinside = Dcinside()

    twicenest.change_option("테스트", "개발 버전 테스트 중입니다.", dev=True)
    want.change_option("테스트", "개발 버전 테스트 중입니다.", dev=True)
    dcinside.change_option("테스트", "개발 버전 테스트 중입니다.", dev=True)

    height = 100

    for mv in mv_list:
        instance = MVInstance(mv, db)
        make.add_mv_dict(instance.get_dict())
        height += 200

    make.make_html()
    take_screen(height)

    twicenest.POST()
    want.POST()
    dcinside.POST()


doWork()

schedule.every().day.at("07:59:40").do(doWork)

while True:
    schedule.run_pending()
    time.sleep(1)
