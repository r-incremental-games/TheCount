import json
import os


class SaveLoad(object):
    BASE_SAVE_DIR = "save"
    HIGHEST_NUMBER_FILE_NAME = os.path.join(BASE_SAVE_DIR, "highest-number.txt")
    STATS_DICT_FILE_NAME = os.path.join(BASE_SAVE_DIR, "stats.txt")

    @staticmethod
    def save_highest_number(number):
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
