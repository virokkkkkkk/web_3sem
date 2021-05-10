# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
enter = input('Введите ip адрес в формате 10.1.1.0/24:')
# enter = '192.168.3.1/24'
# enter = '10.1.1.0/24'
mask = enter.split('/')[-1]
ip = enter.split('/')[0]
# ip = "192.168.3.1"
ip = ip.split('.')
print('Network:')
# print(ip)
for i in ip:
	e = 10 - len(i)
	print(i, end='')
	print(' '*e, end='')
	# for x in range(1,e):
	# 	print(' ',end='')
print()
for i in ip:
	buf = (bin(int(i))).replace('0b','')
	e = 8 - len(buf)
	# for x in range(1,e):
	# 	print('0',end='')
	print('0' * e,end='')
	print(buf,end='  ')
print()
print()

print('Mask:')
print('/'+mask+':')
mask = int(mask)
# Двоичная маска без пробелов
m = '1'*+mask+'0'*(32-mask)
# print(m)
for i in range(4):
	mask_dec = int(m[8*i:8*(i+1)], base=2)
	e = 10 - len(str(mask_dec))
	print(str(mask_dec) + ' '*e, end='')
print()
for i in range(4):
	print(m[8*i:8*(i+1)] + ' '*2, end='')
