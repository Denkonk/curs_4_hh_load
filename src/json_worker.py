import json
import os.path
from config import DATA_PATH
from src.abstract_json_worker import Abstract_json_worker

class Json_worker(Abstract_json_worker):
    def __init__(self, file_name):
        self.file_path = os.path.join(DATA_PATH, file_name)
        self.prepare()

    def prepare(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def add_vacancies(self, vacancies):
        pass

    def get_vacancies(self, keyword):
        pass

    def del_vacancies(self, vacancies):
        pass


