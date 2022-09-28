from abc import ABC, abstractmethod
import requests
import json


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, name, number_vac):
        self.name = name
        self.number_vac = number_vac

    def get_request(self):
        counter = 1
        try:
            with open('vacancy.txt', 'a', encoding='utf-8') as file:
                for i in range(self.number_vac // 10):
                    print(f'Обработка страницы №{i+1}')
                    par = {'text': self.name, 'only_with_salary': True,
                           'per_page': '10', 'page': i, 'area': '113'}
                    response = requests.get('https://api.hh.ru/vacancies/', params=par).json()
                    for j in range(10):
                        try:
                            dict_vacancy = response['items'][j]
                        except KeyError:
                            print('KeyError')
                            continue
                        cl_vacancy = Vacancy(dict_vacancy)
                        file.write(str(counter) + '***' + cl_vacancy.__repr__() + '\n')
                        counter += 1
        except IndexError:
            print('Найдены все доступные вакансии')
            return counter
        return counter
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
        return f'Название вакансии - {self._title_job}--' \
               f'Зарплата - {self._salary_job}--' \
               f'Ссылка - {self._link_job}--' \
               f'Описание: {self._description_job}--'

