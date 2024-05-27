from abc import ABC, abstractmethod

class abstract_json_worker(ABC):
    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    @abstractmethod
    def del_vacancies(self, vacancies):
        pass