# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
mac = mac.replace(':','')

# print(len(mac)/2)
res = ''
for i in range(int(len(mac)/2)):
	buf = mac[i*2:i*2+2]
	res=res+bin(int(buf,16))
	# print(res)
res = res.replace('0b','')	
print(res)