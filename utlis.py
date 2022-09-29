from random import choices
import copy
import re
import heapq
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
    with open('vacancy.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    res = content.split('\n')
    del res[-1]
    dict_sal = {}
    count = 0
    for line in res:
        sal_line = re.findall(r' [0-9]{2,8} ', line)
        if len(sal_line) == 1:
            dict_sal[count] = int(sal_line[0].strip())
        else:
            dict_sal[count] = int((int(sal_line[0].strip()) + int(sal_line[1].strip())) / 2)
        count += 1
    list_key_sal = heapq.nlargest(5, dict_sal, key=dict_sal.get)
    for item in list_key_sal:
        res[item] = ''.join(res[item]).replace('--', '\n').replace('***', '\n').replace('////', '').rstrip('\n')
        print(res[item])

def get_random_vac(counter):
    with open('vacancy.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    res = content.split('\n')
    res = choices(res, k=3)
    for i in range(3):
        res[i] = ''.join(res[i]).replace('--', '\n').replace('***', '\n').replace('////', '').rstrip('\n')
        print(res[i])

def get_ten_first():
    with open('vacancy.txt', 'r', encoding='utf-8') as f:
        res = []
        for line in f:
            s = line.replace('--', '\n').replace('***', '\n').replace('////', '').rstrip('\n')
            if len(res) == 10:
                break
            res.append(s)
        print(*res)
