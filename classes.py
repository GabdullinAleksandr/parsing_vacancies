from abc import ABC, abstractmethod
import requests
import json
from bs4 import BeautifulSoup as BS
import lxml

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

class HH(Engine):
    '''
    Обрабатывает HH через api
    '''
    def __init__(self, name: str, number_vac: int):
        self.name = name
        self.number_vac = number_vac
    def get_request(self):
        counter: int = 1
        try:
            with open('vacancy.txt', 'a', encoding='utf-8') as file:
                for i in range(self.number_vac // 10):
                    print(f'Обработка страницы №{i+1}')
                    par: list = {'text': self.name, 'only_with_salary': True,
                           'per_page': '10', 'page': i, 'area': '113'}
                    response = requests.get('https://api.hh.ru/vacancies/', params=par).json()
                    for j in range(10):
                        dict_vacancy: dict = response['items'][j]
                        cl_vacancy = Vacancy(dict_vacancy)
                        file.write('***' + str(counter) + '***' + cl_vacancy.__repr__() + '\n')
                        counter += 1
        except IndexError:
            print('Найдены все доступные вакансии')
            return counter
        return counter

class Superjob(Engine):
    def __init__(self, request_user, counter):
        self.request_user = request_user
        self.counter = counter
    def get_request(self, rur='RUR', to_sal=None):
        list_name: list = []
        list_description: list = []
        list_salary: list = []

        for page in range(1,4):
            print(f'Обработка страницы №{page}')
            link: str = f'https://russia.superjob.ru/vacancy/search/?keywords={self.request_user}&page={page}'
            response = requests.get(link)
            data_link = BS(response.text, 'lxml')
            name = data_link.find_all('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')
            list_name += name
            description = data_link.find_all('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky')
            list_description += description
            salary = data_link.find_all('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')
            list_salary += salary

        dict_vacancy = {}
        counter = self.counter
        with open('vacancy.txt', 'a', encoding='utf-8') as file:
            for i in range(len(list_name)-1):
                if list_salary[i].text == 'По договорённости':
                    continue
                salary = list_salary[i].text.replace('\xa0','').replace('от','')
                salary = salary.replace('до','').replace('руб.','')
                if len(salary) >= 8:
                    from_sal = salary.split('—')[0]
                    to_sal = salary.split('—')[1]
                else:
                    from_sal = salary
                dict_vacancy = {'name': list_name[i].text,
                                'alternate_url': 'https://russia.superjob.ru/' + list_name[i].a["href"],
                                'snippet': {'responsibility': list_description[i].text},
                                'salary': {'from': from_sal, 'to': to_sal, 'currency': rur}
                                }
                cl_vacancy = Vacancy(dict_vacancy)
                file.write('***' + str(counter) + '***' + cl_vacancy.__repr__() + '\n')
                counter += 1
                to_sal = None
        return counter

class Vacancy():
    '''
    Приводит инфу с сайтов к нужному формату
    '''
    def __init__(self, dict_vacancy: dict):
        self.dict_vacancy = dict_vacancy
        self._title_job: str = self.get_title()
        self._link_job: str = self.get_link()
        self._description_job: str = self.get_description()
        self._salary_job: str = self.get_salary()
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
               f'////Зарплата - {self._salary_job}////--' \
               f'Ссылка - {self._link_job}--' \
               f'Описание: {self._description_job}'

