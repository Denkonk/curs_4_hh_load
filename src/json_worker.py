import json
import os.path
from config import DATA_PATH
from src.abstract_json_worker import AbstractJsonWorker

class Json_worker(AbstractJsonWorker):
    '''
    Класс для сохранения данных о вакансиях в формате JSON в файл
    '''
    def __init__(self, file_name):
        self.file_path = os.path.join(DATA_PATH, file_name)
        self.prepare()

    def prepare(self):
        '''
        Создает файл JSON с пустым списком
        '''
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def add_vacancies(self, vacancies):
        '''
        Сохраняет список вакансий в файл JSON
        '''
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii = False)

    def get_vacancies(self, keyword):
        pass

    def del_vacancies(self, vacancies):
        pass


