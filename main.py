from utlis import *
from classes import *


def create_list_jobs(name):
    while True:
        par = {'text': name, 'only_with_salary': True, 'per_page': 10, 'page': i}
        response = requests.get('https://api.hh.ru/vacancies/', params=par)
    pass

def main():
    request_user = input('Введите ключевое слово для поиска профессии - ')
    create_list_jobs(request_user)
    pass



