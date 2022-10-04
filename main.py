from utlis import *
from classes import *

def main():
    with open('vacancy.txt', 'wb') as f: # Очищает файл
        pass
    request_user: str = input('Введите ключевое слово для поиска профессии - ')
    try:
        number_of_vac_user: int = int(input('Введите требуемое кол-во вакансий с HH(не менее 10) - '))
    except:
        print('incorrect input')
        quit()
    hh = HH(request_user, number_of_vac_user)
    print('Выполняется поиск по HH')
    number_of_vac: int = hh.get_request() - 1
    if number_of_vac == 0:
        print('Вакансий не найдено')
        quit()
    sj = Superjob(request_user, number_of_vac + 1)
    print('Выполняется поиск по SJ')
    number_of_vac = sj.get_request() - 1

    while True:
        print(f'\nНайдено вакансий: {number_of_vac}')
        print('Напишите номер пункта для вызвова или "stop":\n'
              '1 - получить топ десять вакансий по зарплате\n'
              '2 - получить 3 случайные вакансии\n'
              '3 - получить 10 первых вакансий\n')
        user_input: str = input()
        if user_input == 'stop':
            break
        res: list|bool = check_us_inp(user_input)
        if res == False:
            print('incorrect input\nПопробуйте еще раз')
            continue
        else:
            print(*res)


if __name__ == '__main__':
    main()
