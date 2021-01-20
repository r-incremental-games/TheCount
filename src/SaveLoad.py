import json
import os
from pathlib import Path


class SaveLoad(object):
    BASE_SAVE_DIR = "save"
    HIGHEST_NUMBER_FILE_NAME = os.path.join(BASE_SAVE_DIR, "highest-number.txt")
    STATS_DICT_FILE_NAME = os.path.join(BASE_SAVE_DIR, "stats.txt")

    @staticmethod
    def save_highest_number(number):
        Path(SaveLoad.BASE_SAVE_DIR).mkdir(parents=True, exist_ok=True)

        with open(SaveLoad.HIGHEST_NUMBER_FILE_NAME, 'w') as file:
            file.write(json.dumps(number))

    @staticmethod
    def get_highest_number():
        try:
            with open(SaveLoad.HIGHEST_NUMBER_FILE_NAME, 'r') as file:
                lines = ''.join(file.readlines())
                return int(json.loads(lines))
        except:
            return 0

    @staticmethod
    def save_stats_dict(stats):
        Path(SaveLoad.BASE_SAVE_DIR).mkdir(parents=True, exist_ok=True)

        with open(SaveLoad.STATS_DICT_FILE_NAME, 'w') as file:
            file.write(json.dumps(stats))

    @staticmethod
    def get_stats_dict():
        try:
            with open(SaveLoad.STATS_DICT_FILE_NAME, 'r') as file:
                lines = ''.join(file.readlines())
                return json.loads(lines)
        except:
            return {}
