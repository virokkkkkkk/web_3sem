# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    f = open(config_filename)
    intf = ''
    access_dict = {}
    trunk_dict = {}
    isPushed = True
    for line in f:
        if (len(line.strip())>0) and (line[0]!='!'):
            if('interface' in line):
                if isPushed==False:
                    access_dict[intf]=1
                intf = line.replace('interface ','').strip()
                isPushed = False
            if('switchport access vlan' in line):
                access_dict[intf]=int(line.replace('switchport access vlan ', ''))
                isPushed = True
            if('switchport trunk allowed vlan' in line):
                trunk_dict[intf] = list(map(int, line.replace('switchport trunk allowed vlan ', '').strip().split(',')))
                isPushed = True
            # if flag:
            #     print(line,end='')
    f.close()
    return access_dict, trunk_dict
print(get_int_vlan_map('config_sw2.txt'))