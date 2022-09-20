# Part - 4
# Lesson - 21

# Sets

rainbow_colors = {'red', 'orange', 'yellow',
                  'green', 'blue', 'indigo', 'violet'}
# {'indigo', 'orange', 'violet', 'green', 'blue', 'red', 'yellow'}
print(rainbow_colors)
print(type(rainbow_colors))  # <class 'set'>

empty_set = {}
print(empty_set)  # {}
print(type(empty_set))  # <class 'dict'>

empty_set2 = set()
print(empty_set2)  # set()
print(type(empty_set2))  # <class 'set'>

number_list = [1, 2, 3, 1]
text_tuple = ('a', 's', 's', 'f')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)
print(set_from_list)  # {1, 2, 3}
print(set_from_tuple)  # {'a', 'f', 's'}

set_from_list.add(777)
set_from_tuple.add('sss')
print(set_from_list)  # {1, 2, 3, 777}
print(set_from_tuple)  # {'s', 'f', 'sss', 'a'}

y = set_from_list.remove(777)  # Del  item
print(set_from_list)  # {1, 2, 3}

set_from_list.discard(2)
print(set_from_list)  # {1, 3}

x = set_from_list.pop()  # Del random item
print(set_from_list)  # {2, 3}

print(x, y)  # 1 None

# Part - 4
# Lesson - 23

# Booleans

print(1 < 2)
print(type(True))
print(type(False))

# Comparison operators

print(1 == 1)
print(1 == 2)
print('Hello' == 'Hello')
print('Hello' == 'hello')

print(1 != 1)
print(1 != 2)
print('Hello' != 'Hello')
print('Hello' != 'hello')

print(1 > 2)
print(1 < 2)
print(2 >= 2)
print(3 >= 2)
print(2 <= 2)
print(3 <= 2)

print(ord('a'))
print(ord('b'))
print('a' > 'b')
print('hi' > 'hello')
print(ord('i'))
print(ord('e'))

x = 10
y = 23

print(x > y)
print(x < y)
print(x == y)
print(x != y)

age = int(input('Input your age: '))
print('Access is permitted: ' + str(age >= 18))

# Part - 4
# Lesson - 24

# Логические операторы
