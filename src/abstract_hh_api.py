from abc import ABC, abstractmethod

class AbstractHHAPI(ABC):
    '''
    Абстрактный класс, который предоставляет базовую структуру для парсеров вакансий
    '''
    @abstractmethod
    def get_vacancies(self, keyword, count):
        pass





