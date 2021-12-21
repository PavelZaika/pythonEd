# Part - 4
# Lesson - 10

print('Hello World!')

# Part - 4
# Lesson - 12

print(2 ** 3)  # возведение в степень
print(2345 % 2)

# Part - 4
# Lesson - 13

x = 5
type_of_var = type(x)
print(type_of_var)

if type_of_var == int:
    print('done')

# Part - 4
# Lesson - 15

greeting = '0123456789!'
greeting_length = len(greeting)
print(greeting_length)  # длина
print(greeting[0])  # нулевой символ (он же первый)
print(greeting[2:5])  # с 2 по 5(5 не включает)
print(greeting[6:10])  # с 6 по 9 включительно
print(greeting[-5:-2])  # с конца с пятого символа до второго с конца
print(greeting[2:])  # с 2 символа до конца
print(greeting[:5])  # с 0 до 5(с нулевого до 4 включительно)
print(greeting[:])  # все
print(greeting[::2])  # с первого до конца каждые 2
print(greeting[1::3])  # с первого до конца каждый третий
print(greeting[1:9:3])  # с первого символа по 9 через 3 символа
print(greeting[::-1])  # Развернуть строку

# Part - 4
# Lesson - 16

# Multiplication
yummy = 'Yum'
print(yummy * 2)  # YumYum

# Methods
print(yummy.upper())  # YUM
print(yummy.lower())  # yum

long_string = 'This is a long long string'
print(long_string.split())  # ['This', 'is', 'a', 'long', 'long', 'string']
print(long_string.split('s'))  # ['Thi', ' i', ' a long long ', 'tring']

# Part - 4
# Lesson - 17

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', 23)
print(name_and_age)
name_and_age = 'My name is {}. I\'m {} years old.'.format(name, age)
print(name_and_age)

week_days = 'There are 7 days in a week: {1},{2},{3},{4},{5},{6},{0}.'.format(
    'Sun', 'Mon', 'Tue', 'Wed', 'Thus', 'Frid', 'Sat')
print(week_days)  # There are 7 days in a week: Mon,Tue,Wed,Thus,Frid,Sat,Sun.

week_days = 'There are 7 days in a week: {mo},{tu},{we},{th},{fr},{sa},{su}.'.format(
    su='Sun', mo='Mon', tu='Tue', we='Wed', th='Thus', fr='Frid', sa='Sat')
print(week_days)  # There are 7 days in a week: Mon,Tue,Wed,Thus,Frid,Sat,Sun.


float_res = 1000 / 7
print(float_res)
print('The result of division is {0:1.3f}'.format(float_res))
print(f'The result of division is {float_res:1.3f}')
print(f'The result of division is {float_res:1.7f}')


name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = f'My name is {name}. I\'m {age} years old.'
print(name_and_age)
