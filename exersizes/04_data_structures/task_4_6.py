# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route = ospf_route.split(', ')
firstpart = ospf_route[0].split(' ')
prefix = firstpart[-4]
AD = firstpart[-3]
nextHop = firstpart[-1]
lastUpdate = ospf_route[-2]
OInterface = ospf_route[-1]
# print(ospf_route)
# print(prefix)

print('Prefix                '+prefix)
print('AD/Metric             '+AD[1:-1])
print('Next-Hop              '+nextHop)
print('Last update           '+lastUpdate)
print('Outbound Interface    '+OInterface)
# Prefix                10.0.24.0/24
# AD/Metric             110/41
# Next-Hop              10.0.13.3
# Last update           3d18h
# Outbound Interface    FastEthernet0/0