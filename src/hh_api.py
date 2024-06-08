from src.abstract_hh_api import AbstractHHAPI
import requests

class HHAPI(AbstractHHAPI):
    """
    Использует API HH.ru для получения списка вакансий, соответствующих заданному запросу
    """
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies/"
        self.params = {
            'text': '',
            'page': 0,
            'per_page': 100,
            'only_with_salary': True,
            'area': 113
        }

    def get_vacancies(self, keyword, count):
        '''
        Получает список вакансий с API HH.ru
        '''
        self.params.update({'text': keyword})
        vacancies = []
        pages = count // self.params['per_page'] + (1 if count % self.params['per_page'] else 0)

        for page in range(pages):
            self.params['page'] = page
            response = requests.get(self.url, params=self.params)
            data = response.json()
            vacancies.extend(data['items'])

            if len(vacancies) >= count:
                break

        return vacancies[:count]

# if __name__ == '__main__':
#     my_api = HH_API()
#     response = my_api.get_vacancies('водитель', 100)
#     print(response)


