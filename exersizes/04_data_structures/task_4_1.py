# -*- coding: utf-8 -*-
"""
Задание 4.1

Используя подготовленную строку nat, получить новую строку, в которой
в имени интерфейса вместо FastEthernet написано GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
# nat = ' djfnasdk fhdkfjhf jkasdhkf hk FastEthernet0/1 overload'
print(nat)

nat.replace('FastEthernet0','GiGabitEthernet0')
print(nat)

nat = nat.replace('FastEthernet0','GiGabitEthernet0')
print(nat)