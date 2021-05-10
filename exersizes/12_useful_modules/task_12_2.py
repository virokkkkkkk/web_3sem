# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
def convert_ranges_to_ip_list(ranges):
    """
    Элементы списка могут быть в формате:
    * 10.1.1.1
    * 10.1.1.1-10.1.1.10
    * 10.1.1.1-10

    Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
    Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.
    """
    resultRanges = []
    for oneRange in ranges:
        # print(len(oneRange.split('.')), len(oneRange.split('-')))
        
        r = oneRange.split('.')
        beginOfIp = r[0]+'.'+r[1]+'.'+r[2]+'.'
        first = int(r[3].split('-')[0])
        # '10.1.1.1-10.1.1.10' формат
        if len(r) == 7:
            last = int(r[-1])
            for i in range(first, last+1):
                resultRanges.append(beginOfIp+str(i))

        # '10.1.1.1-10' формат
        elif len(r) == 4 and len(oneRange.split('-'))==2:
            last = int(oneRange.split('-')[-1])
            for i in range(first, last+1):
                resultRanges.append(beginOfIp+str(i))
        # '10.1.1.1' формат
        else:
            resultRanges.append(oneRange)
        

    return resultRanges


if __name__ == '__main__':
    a = ['10.1.1.1', '10.1.1.1-10.1.1.10', '10.1.1.1-10']
    print(convert_ranges_to_ip_list(a))