# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(ipAddresses):
    availableList = []
    unavailableList = []
    for ip in ipAddresses:
        result = subprocess.run(['ping', '-n', '2', ip],
                           stdout=subprocess.PIPE)
        # result = subprocess.run(['ping', '-n', '2', ip], stdout=subprocess.PIPE)
        if(result.returncode==0):
            availableList.append(ip)
        else:
            unavailableList.append(ip)
    return (availableList, unavailableList)

if __name__ == '__main__':
    list_of_ips = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    return_value = ping_ip_addresses(list_of_ips)
    print(return_value)