#!/usr/bin/python3
# coding: utf8

while True:
	try:
		exit =input('Для прекращение работы программы введите exit для продолжения нажмите enter  ')
		if exit =='exit':
			break
		a=int(input('Введите точку А '))
		b=int(input('Введите точку B '))
		c = list()
		assert a < b
	except AssertionError:
		print("Неправильно задан отрезок")
	else:
		for numbers in range(a-1,b):
			numbers +=1;
			c.append(numbers)
		print('сумма = ' + str(sum(c)))
		print('длина = ' + str(len(c)))
		value =(sum(c))/(len(c))
		print('среднее арифметическое всех чисел из отрезка равно ' + str(value))
		print('-------------------')

print('программа завершена')
	
	