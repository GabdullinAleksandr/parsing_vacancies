from utlis import *
from classes import *
import json

# par = {'text': 'python', 'only_with_salary': True, 'per_page': 10, 'page': 1}
# response = requests.get('https://api.hh.ru/vacancies/', params=par).json()
# with open('', 'w', encoding='utf-8') as file_jobs:
#     json.dump(response.json(), file_jobs, indent=4, ensure_ascii=False)




def main():
    # with open('vacancy.txt', 'wb') as f:
    #     pass


    request_user = input('Введите ключевое слово для поиска профессии - ')
    head_h = HH(request_user)
    head_h.get_request()


if __name__ == '__main__':
    main()
