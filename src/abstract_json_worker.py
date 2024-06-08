from abc import ABC, abstractmethod

class AbstractJsonWorker(ABC):
    '''
    Абстрактный метод для сохранения и чтения из файла
    '''
    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    @abstractmethod
    def del_vacancies(self, vacancies):
        pass
