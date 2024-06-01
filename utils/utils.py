from src.json_worker import Json_worker
from src.hh_api import HH_API

def user_interaction():
    json_worker = Json_worker('vacancies.json')
    api_hh = HH_API()
    vacancies = api_hh.get_vacancies('водитель', 100)
    json_worker.add_vacancies(vacancies)

if __name__ == '__main__':
    user_interaction()

