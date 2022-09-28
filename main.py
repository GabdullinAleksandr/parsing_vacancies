from utlis import *
from classes import *
import json
from random import randint
def check_us_inp(user, number_of_vac):
    check = user.isdigit()
    if check == False:
        return False
    elif user == '1':
        get_top_five()
    elif user == '2':
        get_random_vac(number_of_vac)
    elif user == '3':
        get_ten_first()
    elif user == '4':
        get_ten_if()
    else:
        return False
def get_top_five():
    pass
def get_random_vac(counter):
    random_num = randint(1,counter)
    with open('vacancy.txt', 'r', encoding='utf-8') as f:
        res = list(filter(lambda line: f'***{str(random_num)}***' in line, f))
        res = ''.join(res).replace('--','\n').replace('***','\n')
        print(res)
def get_ten_first():
    with open('vacancy.txt', 'r', encoding='utf-8') as f:
        res = []
        for line in f:
            s = line.replace('--', '\n').replace('***', '\n').rstrip('\n')
            if len(res) == 10:
                break
            res.append(s)
        print(*res)
def get_ten_if():
    pass

def main():
    with open('vacancy.txt', 'wb') as f:
        pass
    request_user = input('Введите ключевое слово для поиска профессии - ')
    try:
        number_of_vac_user = int(input('Введите требуемое кол-во вакансий(не менее 10) - '))
    except:
        print('incorrect input')
        quit()
    head_h = HH(request_user, number_of_vac_user)
    print('Выполняется поиск по HH')
    number_of_vac = head_h.get_request() - 1
    if number_of_vac == 0:
        print('Вакансий не найдено')
        quit()
    while True:
        print(f'Найдено вакансий: {number_of_vac}')
        print('Напишите номер пункта для вызвова или "stop":\n'
              '1 - получить топ пять вакансий по зарплате\n'
              '2 - получить 3 случайные вакансии\n'
              '3 - получить 10 первых вакансий\n'
              '4 - получить 10 вакансий с зарплатой выше 300000 руб.\n')
        user_input = input()
        if user_input == 'stop':
            break
        if check_us_inp(user_input, number_of_vac) == False:
            print('incorrect input\nПопробуйте еще раз')
            continue

if __name__ == '__main__':
    main()
