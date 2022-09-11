import pymysql
from src.utils.environment import Environment
from src.utils.logger import logger


class Database:
    def __init__(self):
        env = Environment()
        self.host = env.get("DB_HOST")
        self.port = int(env.get("DB_PORT"))
        self.user = env.get("DB_USER")
        self.password = env.get("DB_PASSWORD")
        self.database = env.get("DB_DATABASE")
        self.connect()
        self._check_table()

    def _check_table(self):
        try:
            self.execute("SELECT * from data;")
        except pymysql.err.ProgrammingError:
            self.execute("""CREATE TABLE `data` (
            `date` varchar(27) NOT NULL,
            `name` varchar(4) NOT NULL,
            `viewcount` int(11) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.database, charset='utf8')
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def fetch(self):
        return self.cursor.fetchall()

    def ping(self):
        return self.connection.ping(reconnect=True)

    def close(self):
        self.cursor.close()
        self.connection.close()
