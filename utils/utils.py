from src.json_worker import Json_worker
from src.hh_api import HHAPI
from src.vacancy import Vacancy


def get_vacancies_by_salary(vacancies, salary_min):
    '''
    Фильтрация по зарплате
    '''
    filtered_by_salary = []

    for vacancy in vacancies:
        if vacancy.salary and 'from' in vacancy.salary:
            if vacancy.salary['from'] is not None and vacancy.salary['from'] > salary_min:
                filtered_by_salary.append(vacancy)
    return filtered_by_salary


def print_formatted_vacancies(vacancies):
    '''
    Форматированный вывод вакансий
    '''
    for vacancy in vacancies:
        title = vacancy.title
        city = vacancy.city
        salary_from = vacancy.salary_from
        salary_to = vacancy.salary_to
        requirement = vacancy.requirement
        responsibility = vacancy.responsibility
        schedule = vacancy.schedule
        url = vacancy.url
        created_at = vacancy.created_at

        salary = f"от {salary_from} руб." if salary_to == 0 else f"от {salary_from} до {salary_to} руб."

        print(f"Название вакансии: {title}")
        print(f"Город: {city}")
        print(f"Зарплата: {salary}")
        print(f"Требования: {requirement}")
        print(f"Обязанности: {responsibility}")
        print(f"График работы: {schedule}")
        print(f"Ссылка на вакансию: {url}")
        print(f"Дата создания вакансии: {created_at}")
        print("\n" + "=" * 50 + "\n")


def user_interaction():
    '''
    Функция взаимодействия с пользователем для поиска вакансий и их сохранения
    '''
    json_worker = Json_worker('vacancies.json')
    api_hh = HHAPI()

    #Ввод данных от пользователем
    search_query = input("Введите поисковый запрос (наименование интересующей вакансии):\n")
    salary_min = int(input("Введите минимальную зарплату:\n"))
    all_vac = int(input("Введите общее количество вакансий:\n"))
    top_n = int(input("Введите количество вакансий для вывода в ТОП N:\n"))

    vacancies_list = api_hh.get_vacancies(search_query, all_vac)
    vacancies = sorted(Vacancy.create_vacansies(vacancies_list), reverse = True)
    vacancies_min_salary = get_vacancies_by_salary(vacancies, salary_min)
    top_vacancies = vacancies_min_salary[:top_n]
    vacancies_result = [item.to_json() for item in top_vacancies]
    json_worker.add_vacancies(vacancies_result)

    print(f"Всего вакансий: {len(vacancies_list)}")
    print(f"Количество вакансий после фильтрации: {len(vacancies_min_salary)}")
    print(f"Количество вакансий в ТОП {top_n}: {len(top_vacancies)}\n")

    print_formatted_vacancies(top_vacancies)




# if __name__ == '__main__':
#     user_interaction()

