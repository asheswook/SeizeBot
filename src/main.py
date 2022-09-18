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


def doWork(file_name: str or list):
    logger.info("Load music video file list...")
    mv_list_file = open(f"{file_name}.json", encoding='utf-8')
    mv_list = json.load(mv_list_file)

    logger.info("Let's work!")
    db.ping()

    make = Make()

    twicenest = Twicenest()
    want = Want()
    dcinside = Dcinside("twiceyou")

    twicenest.change_option("[08:00] TWICE 뮤비 조회수",
                            """뮤비봇의 V3 버전이 릴리즈 되었습니다.
                            개발자분들의 많은 관심 부탁드립니다.
                            https://github.com/asheswook/SeizeBotV3""", dev=False)
    want.change_option("[08:00] TWICE 뮤비 조회수", """뮤비봇의 V3 버전이 릴리즈 되었습니다.
                            개발자분들의 많은 관심 부탁드립니다.
                            https://github.com/asheswook/SeizeBotV3""", dev=False)
    dcinside.change_option("[08:00] TWICE 뮤비 조회수", """뮤비봇의 V3 버전이 릴리즈 되었습니다.
                            개발자분들의 많은 관심 부탁드립니다.
                            https://github.com/asheswook/SeizeBotV3""", dev=False)

    height = 70

    for mv in mv_list:
        instance = MVInstance(mv, db)
        make.add_mv_dict(instance.get_dict())
        height += 110

    make.make_html()
    take_screen(height)

    twicenest.POST()
    want.POST()
    dcinside.POST()

    logger.info("All works done!")


schedule.every().day.at("07:59:40").do(doWork, "mv_list")

while True:
    logger.info("Waiting for...")
    schedule.run_pending()
    time.sleep(1)
