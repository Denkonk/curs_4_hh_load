from src.json_worker import Json_worker
from src.hh_api import HH_API
from src.vacancy import Vacancy

def user_interaction():
    json_worker = Json_worker('vacancies.json')
    api_hh = HH_API()
    #input()
    vacancies_list = api_hh.get_vacancies('водитель', 100)
    vacancies = sorted(Vacancy.create_vacansies(vacancies_list), reverse = True)
    vacancies = [item.to_json() for item in vacancies]
    json_worker.add_vacancies(vacancies)


if __name__ == '__main__':
    user_interaction()

