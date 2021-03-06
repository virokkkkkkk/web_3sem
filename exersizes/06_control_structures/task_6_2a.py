# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

import re
ip = input('Введите IP в формате 10.0.1.1 ')
# ip = '10.0.1.1'
f = ip.split('.')[0]
f = int(f)
# print(f)
res = ''

match = re.fullmatch(r'^((25[0-5]|((2[0-4]|1\d|\d?)\d))\.){3}(25[0-5]|((2[0-4]|1\d|\d?)\d))$',ip)

if match==None:
    res = 'Неправильный IP-адрес'
elif (f>=1) and (f<=223):
    res = '«unicast»'
elif f>=224 and f<=239:
    res = '«multicast»'
elif ip=='255.255.255.255':
    res = 'local broadcast'
elif ip=='0.0.0.0':
    res = '«unassigned»'
else:
    res = 'unused'
print(res)