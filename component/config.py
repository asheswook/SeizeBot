import os
import json
from functools import cache


class Config:
    def __init__(self, file_path: str, is_main_config: bool = False):
        self.file_path = file_path
        self.is_main_config = is_main_config

    @cache
    def check_file(self):
        print(f'{self.file_path} is checking...')
        if os.path.isfile(self.file_path):
            print('Config file found.')
            return True
        else:
            if self.is_main_config:
                if os.path.isfile('./._setting.json'):
                    print(
                        "Default config file has detected. Please rename it to '.setting.json'")
            print(
                f'*WARNING* Cannot read config file. ({self.file_path}) Please check your config file.')
            return False

    def load_config(self):
        if self.check_file():
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return False

    def load_config_piece(self, piecename: str):
        if self.check_file():
            with open(self.file_path, 'r') as file:
                return json.load(file).get(piecename)
        else:
            return False


config = Config('./.setting.json', True)
mysql_config = config.load_config_piece('mysql')
twicenest_config = config.load_config_piece('twicenest')
want_config = config.load_config_piece('want')
wiki_config = config.load_config_piece('twicewiki')
