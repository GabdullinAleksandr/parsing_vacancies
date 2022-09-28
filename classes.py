from abc import ABC, abstractmethod
import requests
import json


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, name):
        self.name = name

    def get_request(self):
        with open('vacancy.txt', 'a', encoding='utf-8') as file:
            for i in range(5):
                par = {'text': self.name, 'only_with_salary': True,
                       'per_page': '10', 'page': i, 'area': '113'}
                response = requests.get('https://api.hh.ru/vacancies/', params=par).json()
                for j in range(10):
                    dict_vacancy = response['items'][j]
                    cl_vacancy = Vacancy(dict_vacancy)
                    file.write('\n' + cl_vacancy.__repr__() + '---')

class Superjob(Engine):
    def get_request(self):
        pass

class Vacancy():
    def __init__(self, dict_vacancy):
        self.dict_vacancy = dict_vacancy
        self._title_job = self.get_title()
        self._link_job = self.get_link()
        self._description_job = self.get_description()
        self._salary_job = self.get_salary()
    def get_title(self):
        return self.dict_vacancy['name']
    def get_link(self):
        return self.dict_vacancy['alternate_url']
    def get_description(self):
        return self.dict_vacancy['snippet']['responsibility']
    def get_salary(self):
        return f"{self.dict_vacancy['salary']['from']} - " \
               f"{self.dict_vacancy['salary']['to']} " \
               f"{self.dict_vacancy['salary']['currency']}"

    def __repr__(self):
        return f'Название вакансии - {self._title_job}\n' \
               f'Зарплата - {self._salary_job}\n' \
               f'Ссылка - {self._link_job}\n' \
               f'Описание: {self._description_job}\n'

