
# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

enter = argv[1]
# выполняется командой:
# python 5.2a.py 10.40.25.56/20

# адрес хоста
# enter = '10.40.25.56/20'

mask = enter.split('/')[-1]
ip = enter.split('/')[0]
ip = ip.split('.')

# Двоичная маска без пробелов
mask = int(mask)
m = '1'*+mask+'0'*(32-mask)
# print('m = ' + m)

# выводим адрес сети:
print('Network:')

# вывод нового адреса сети
# и формируем новый ip
j = 0
new_ip = []
for i in ip:
	mask_dec = int(m[8*j:8*(j+1)], base=2)
	# побитовое умножение маски и ip
	buf = str(int(i) & mask_dec)
	print(f'{buf}{" "*(10-len(buf))}', end='')
	new_ip.append(int(buf))
	j+=1
print()

for i in new_ip:
	buf = (bin(int(i))).replace('0b','')
	e = 8 - len(buf)
	print(f'{"0" * e}{buf}  ', end='')
print()
print()

print('Mask:')
print('/'+str(mask)+':')

for i in range(4):
	mask_dec = int(m[8*i:8*(i+1)], base=2)
	e = 10 - len(str(mask_dec))
	print(f'{str(mask_dec) + " "*e}', end='')
print()
for i in range(4):
	print(m[8*i:8*(i+1)] + ' '*2, end='')