# Part - 4
# Lesson - 18

# Lists

from operator import ne


number_list = [32, 323, 2, 1, 1.2, '2Two']
print(number_list)  # [32, 323, 2, 1, 1.2, '2Two']

print(len(number_list))  # 6

print(number_list[1])  # 323

# формирует новый список с 0позиции и до указанного элемента
new_list = number_list[:2]
print(new_list)  # [32, 323]

number_list[5] = '3Three'  # меняет значение на указанной позиции
print(number_list)  # [32, 323, 2, 1, 1.2, '3Three']

one_more_list = number_list + new_list  # сложение листов
print(one_more_list)  # [32, 323, 2, 1, 1.2, '3Three', 32, 323]

new_list.append('new item')  # добавляет указанное значение в конец листа
print(new_list)  # [32, 323, 'new item']

# добавляет указанное значение на указанную позицию
new_list.insert(0, 'start')
print(new_list)  # ['start', 32, 323, 'new item']

new_list.pop()  # удаляет последний элемент
print(new_list)  # ['start', 32, 323]

new_list.pop(0)  # удалит элемент с указанным индексом
print(new_list)  # [32, 323]

# удаляет последний элемент и добавляет его в переменную
deleted_item = number_list.pop()
print(number_list)  # [32, 323, 2, 1, 1.2]
print(deleted_item)  # 3Three

print(number_list)  # [32, 323, 2, 1, 1.2]
# удаляет по значению, но удаляет только первый попавшийся элемент
deleted_item = number_list.remove(1.2)
print(number_list)  # [32, 323, 2, 1]
print(deleted_item)  # None

one_list = [1, 2, 3, 45, 89, 12, 5]
letter_list = ['a', 'd', 's', 'q', 'a', 'y', 'c']
print(one_list)  # [1, 2, 3, 45, 89, 12, 5]
one_list.sort()  # сортировка
print(one_list)  # [1, 2, 3, 5, 12, 45, 89]

print(letter_list)  # ['a', 'd', 's', 'q', 'a', 'y', 'c']
letter_list.sort()  # сортировка
print(letter_list)  # ['a', 'a', 'c', 'd', 'q', 's', 'y']

one_list.reverse()  # разворачивает список
print(one_list)  # [89, 45, 12, 5, 3, 2, 1]


# Part - 4
# Lesson - 19

# Dictionaries

car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000}
print(car_prices)  # {'opel': 5000, 'toyota': 7000, 'bmw': 10000}

print(car_prices['toyota'])  # 7000
car_prices['mazda'] = 4000

# {'opel': 5000, 'toyota': 7000, 'bmw': 10000, 'mazda': 4000}
print(car_prices)

car_prices['opel'] = 2000
# {'opel': 2000, 'toyota': 7000, 'bmw': 10000, 'mazda': 4000}
print(car_prices)

del car_prices['toyota']
print(car_prices)  # {'opel': 2000, 'bmw': 10000, 'mazda': 4000}

car_prices.clear()
print(car_prices)  # {}

person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daughter': 'Pamela'}
}

print(person['age'])  # 43

print(person['hobbies'])  # ['football', 'singing', 'photo']

hobbies = person['hobbies']
print(hobbies[2])  # photo
print(person['hobbies'][2])  # photo

children = person['children']
print(children['son'])  # Michael
print(person['children']['son'])  # Michael

person['car'] = 'Mazda'
print(person['car'])  # Mazda

person['hobbies'][0] = 'basketball'
print(person['hobbies'])  # ['basketball', 'singing', 'photo']

# dict_keys(['first name', 'last name', 'age', 'hobbies', 'children', 'car'])
print(person.keys())

# dict_values(['Jack', 'Brown', 43, ['basketball', 'singing', 'photo'], {'son': 'Michael', 'daughter': 'Pamela'}, 'Mazda'])
print(person.values())

# dict_items([('first name', 'Jack'), ('last name', 'Brown'), ('age', 43), ('hobbies', ['basketball', 'singing', 'photo']), ('children', {'son': 'Michael', 'daughter': 'Pamela'}), ('car', 'Mazda')])
print(person.items())

# Part - 4
# Lesson - 20

# Tuples

tuple_1 = 1, 2, 3
tuple_2 = ('one', 'hello')
tuple_3 = (3, 2.3, 'three')


print(type(tuple_1))  # <class 'tuple'>

print(tuple_1)  # (1, 2, 3)
print(tuple_2)  # ('one', 'hello')
print(tuple_3)  # (3, 2.3, 'three')

# tuple_1[1] = 3 # TypeError: 'tuple' object does not support item assignment

print(tuple_1[0])  # 1

new_tuple = (tuple_1[0], 3, tuple_1[-1])
print(new_tuple)  # (1, 3, 3)

# Example
x = y = z = 12
print(x, y, z)  # 12 12 12
x, y, z = 12, 13, 14
print(x, y, z)  # 12 13 14

person_tuple = ('John', 'Smith', 1988)
first_name, last_name, year_of_birth = person_tuple
print(first_name, last_name, year_of_birth)  # John Smith 1988

t1 = (1, 2, 5, 1, 7, 9)
print(t1.count(1))  # 2

greetings_tuple = ('hi', 'hello', 'hi')
print(greetings_tuple.count('hi'))  # 2

print(t1.index(7))  # 4
