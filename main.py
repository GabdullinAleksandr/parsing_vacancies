from utlis import *
from classes import *
from random import choices
import copy
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
    # with open('vacancy.txt', 'r', encoding='utf-8') as f:
    #     content = f.read()
    # res = content.split('\n')
    # del res[-1]
    # # for i in range(len(res)+1):
    # res_salary = copy.deepcopy(res)
    # res_salary = list(map(lambda line: line.split('////')[1], res_salary))
    # total = 0
    # for i in range(len(res_salary)+1):
    #     sal_from = res_salary[i].split('')[2]
    #     sal_to = res_salary[i].split('')[-2]
    #     if sal_from.isditit() and sal_to.isditit():
    #         average_sal = (sal_to + sal_from) / 2
    #         if average_sal
    #
    # print(res_salary)
    pass
def get_random_vac(counter):
    with open('vacancy.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    res = content.split('\n')
    res = choices(res,k=3)
    for i in range(3):
        res[i] = ''.join(res[i]).replace('--','\n').replace('***','\n').replace('////','').rstrip('\n')
        print(res[i])
def get_ten_first():
    with open('vacancy.txt', 'r', encoding='utf-8') as f:
        res = []
        for line in f:
            s = line.replace('--', '\n').replace('***', '\n').replace('////','').rstrip('\n')
            if len(res) == 10:
                break
            res.append(s)
        print(*res)

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

# if __name__ == '__main__':
#     main()

super_job = Superjob
request_user = '1232'
super_job.get_request(request_user)
