
class Vacancy:
    '''
    Класс представления вакансии
    '''
    def __init__(self, title, city, salary, requirement, responsibility, schedule, url, created_at):
        self.title = title
        self.city = city
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.schedule = schedule
        self.url = url
        self.created_at = created_at
        self.validate()

    def validate(self):
        '''
        Проверка на отсутствие зарплаты и отсутствие описании и требований к вакансии
        '''
        if not self.salary:
            self.salary_from = 0
            self.salary_to = 0

        if not self.salary['from']:
            self.salary_from = 0
        else:
            self.salary_from = self.salary['from']

        if not self.salary['to']:
            self.salary_to = 0
        else:
            self.salary_to = self.salary['to']

        #разделить на 2 разных метода
        if not self.requirement:
            self.requirement = ""

        if not self.responsibility:
            self.responsibility = ""

    @classmethod
    def create_vacansies(cls, vacancies_data):
        """
        Создание объектов вакансий согласно необходимых параметров
        """
        instances = []
        for vac_info in vacancies_data:
            title = vac_info['name']
            city = vac_info['area']['name']
            salary = vac_info['salary']
            requirement = vac_info['snippet']['requirement']
            responsibility = vac_info['snippet']['responsibility']
            schedule = vac_info['schedule']['name']
            url = vac_info['alternate_url']
            created_at = vac_info['created_at']
            vacancy = cls(title, city, salary, requirement, responsibility, schedule, url, created_at)
            instances.append(vacancy)
        return instances

    def to_json(self):
        """
        Преобразование объектов вакансий в список словарей вакансий
        """
        return {
            "title": self.title,
            "city": self.city,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
            "schedule": self.schedule,
            "url": self.url,
            "created_at": self.created_at
        }

    def __lt__(self, other):
        """
        Метод для сортировки вакансий по заработной плате
        """
        if isinstance(other, Vacancy):
            return self.salary_from < other.salary_from












