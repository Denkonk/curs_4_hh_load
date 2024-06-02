
class Vacancy:
    def __init__(self, title, city, salary, requirement, responsibility, url, created_at):
        self.title = title
        self.city = city
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.url = url
        self.created_at = created_at
        self.validate()

    def validate(self):
        if not self.salary:
            if not self.salary_from:
                self.salary_from = 0
            if not self.salary_to:
                self.salary_to = 0






