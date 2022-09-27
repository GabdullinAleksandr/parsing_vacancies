from abc import ABC, abstractmethod
import requests
import json

par = {'text': 'python', 'only_with_salary': True, 'per_page': 10, 'page': 1}
response = requests.get('https://api.hh.ru/vacancies/', params=par)
with open('jobs.json', 'w', encoding='utf-8') as file_jobs:
    json.dump(response.json(), file_jobs, indent=4, ensure_ascii=False)

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, name):
        self.name = name

    def get_request(self):
        pass


class Superjob(Engine):
    def get_request(self):
        pass


class Vacancy():
    def __init__(self):
        self.title_job = title_job
        self.link_job = link_job
        self.description_job = description_job
        self.salary_job = salary_job


    def __repr__(self):
        dict_vacancy = {'Название': {self.title_job}, 'Ссылка': {self.link_job},
                        'Описание': {self.description_job}, 'Зарплата': {self.salary_job}}
        return dict_vacancy
    pass

