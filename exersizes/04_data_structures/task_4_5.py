# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command1 = command1.split(' ')[-1]
command1 = command1.split(',')

command2 = command2.split(' ')[-1]
command2 = command2.split(',')

# Из строк command1 и command2 получить список VLANов,
# которые есть и в команде command1
# команде command2 (пересечение).

# Результатом должен быть такой список: ["1", "3", "8"]

# Ограничение: Все задания надо выполнять используя 
# только пройденные темы.

res = set(command1) & set(command2)
# for i in command1:
# 	for j in command2:
# 		if i == j:
# 			res.add(i)
# 			command1.remove(i)
# 			command2.remove(i)

res = list(res)
res.sort()
# print(command1)
# print(command2)
# print()
print(res)