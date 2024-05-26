from src.abstract_hh_api import Abstract_hh_API
import requests

class HH_API(Abstract_hh_API):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies/"
        self.params = {
            'text': '',
            'page': 0,
            'per_page': 200
        }

    def get_vacancies(self, keyword, count):
        self.params.update({'text': keyword})
        response = requests.get(self.url, params=self.params)
        return response

if __name__ == '__main__':
    my_api = HH_API()
    response = my_api.get_vacancies('водитель', 100)
    print(response)


