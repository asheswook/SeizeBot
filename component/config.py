import os
import json


class configClass:
    def __init__(self, filepath, isMainConfigFile=False):
        self.filepath = filepath
        self.isMainConfigFile = isMainConfigFile

    def checkFile(self):
        print(f'{self.filepath} is checking...')
        if os.path.isfile(self.filepath):
            print('Config file found.')
            return True
        else:
            if self.isMainConfigFile:
                if os.path.isfile('./._setting.json'):
                    print(
                        "Default config file has detected. Please rename it to '.setting.json'")
            print(
                f'*WARNING* Cannot read config file. ({self.filepath}) Please check your config file.')
            return False

    def loadConfig(self):
        if self.checkFile():
            with open(self.filepath, 'r') as file:
                return json.load(file)
        else:
            return False

    def loadConfigPiece(self, piecename):
        if self.checkFile():
            with open(self.filepath, 'r') as file:
                return json.load(file).get(piecename)
        else:
            return False


mainConfig = configClass('./.setting.json', True)
mysqlConfig = mainConfig.loadConfigPiece('mysql')
tnConfig = mainConfig.loadConfigPiece('twicenest')
wtConfig = mainConfig.loadConfigPiece('want')
wkConfig = mainConfig.loadConfigPiece('twicewiki')
