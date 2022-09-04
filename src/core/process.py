from multiprocessing import Process
from src.executors.make import Make
from src.utils.database import Database
from src.core.instance import MVInstance


class MyProcess(Process):
    def __init__(self, mv, make, db):
        Process.__init__(self)
        self.mv = mv
        self.db: Database = db
        self.make: Make = make

    def run(self):
        instance = MVInstance(self.mv, self.db)
        self.make.add_mv_dict(instance.get_dict())
