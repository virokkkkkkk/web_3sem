# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

my = {
    'access':[],
    'trunk':[]
}
my['access']=access_template
my['trunk']=trunk_template
# print(my)

request = {
    'access': 'Введите номер VLAN:',
    'trunk': 'Введите разрешенные VLANы:'
}
mode = input('Введите режим работы интерфейса (access/trunk): ')
# mode = 'trunk'
# interface = input('Введите тип и номер интерфейса: ')
interface = 'Fa0/7'

vlans = input(request[mode])
vlans = '2,3,4,5'

print()
print('interface '+interface)
l = my[mode]
# print(l)

s = str(l).replace(', ','\n').replace("'",'')[1:-1].format(vlans)
print(s)