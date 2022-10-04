from random import choices
import re
import heapq

def check_us_inp(user: str) -> list|bool:
    '''
    Чекает ввод пользовотеля и выдает нужную инфу
    :param user: ввод пользователя из main
    :return: False, если некорректный ввод, либо лист с обработанной инфой
    '''
    with open('vacancy.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    list_vacancy: list = content.split('\n')
    list_vacancy.pop()
    match user:
        case '1':
            res = []
            list_key: list = get_top_ten(list_vacancy)
            [res.append(list_vacancy[i]) for i in list_key]
        case '2':
            res: list = choices(list_vacancy, k=3)
        case '3':
            res: list = list_vacancy[:10]
        case _:
            return False
    for item in range(len(res)):
        res[item] = ''.join(res[item]).replace('--', '\n').replace('***', '\n').replace('////', '').rstrip('\n')
    return res

def get_top_ten(content: str) -> list:
    '''
    Считает топ 10 по ЗП
    :param content: данные из файла
    :return: лист с индексами, в отсортированном порядке.
    '''
    dict_sal, count = {}, 0
    for line in content:
        sal_line: str = re.findall(r' [0-9]{2,8} ', line)
        if len(sal_line) == 1:
            dict_sal[count] = int(sal_line[0].strip())
        elif len(sal_line) == 2:
            dict_sal[count] = int((int(sal_line[0].strip()) + int(sal_line[1].strip())) / 2)
        else: continue
        count += 1
    return heapq.nlargest(10, dict_sal, key=dict_sal.get)
