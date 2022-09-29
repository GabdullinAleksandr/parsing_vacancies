from utlis import *
from classes import *

def main():
    with open('vacancy.txt', 'wb') as f:
        pass
    request_user = input('Введите ключевое слово для поиска профессии - ')
    try:
        number_of_vac_user = int(input('Введите требуемое кол-во вакансий с HH(не менее 10) - '))
    except:
        print('incorrect input')
        quit()
    head_h = HH(request_user, number_of_vac_user)
    print('Выполняется поиск по HH')
    number_of_vac = head_h.get_request() - 1
    if number_of_vac == 0:
        print('Вакансий не найдено')
        quit()
    sj = Superjob(request_user, number_of_vac + 1)
    print('Выполняется поиск по SJ')
    number_of_vac = sj.get_request() - 1
    while True:
        print(f'\nНайдено вакансий: {number_of_vac}')
        print('Напишите номер пункта для вызвова или "stop":\n'
              '1 - получить топ пять вакансий по зарплате\n'
              '2 - получить 3 случайные вакансии\n'
              '3 - получить 10 первых вакансий\n')
        user_input = input()
        if user_input == 'stop':
            break
        if check_us_inp(user_input, number_of_vac) == False:
            print('incorrect input\nПопробуйте еще раз')
            continue

if __name__ == '__main__':
    main()


