# Part - 4
# Lesson - 25

# if elif else

# x = 4
#
# if x > 3:
#     print('x > 3')
#     print('I\'m happy')
# elif x < 3:
#     print('x < 3')
# else:
#     print('x == 3')

# day_time = 'midnight'
#
# if day_time == 'morning':
#     print('Monster wakes up')
# elif day_time == 'afternoon':
#     print('Monster is walking')
# elif day_time == 'evening':
#     print('Monster is eating')
# elif day_time == 'night':
#     print('Monster is sleeping')
# else:
#     print('Monster is doing something')

# x = 41
# if x % 2 == 0:
#     print('x is even')
# else:
#     print('x is odd')
# print('Some text')

# user_input = input('Input something')
# if user_input == 'Hello':
#     print('Hello! Nice to meet you!')


# # False: 0, empty string, None, empty object
#
# if [1, 3]:
#     print('Something')

lucky_number = input('Enter a number')
if lucky_number:
    print(lucky_number + ' is your lucky number!')
else:
    print('You have to enter some number, please try again')

# Part - 4
# Lesson - 26

# forLoop

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in number_list:
#     print(str(number) + ' Hola!')

# for number in number_list:
#     if number % 2 == 0:
#         print(number)
#     else:
#         print('Hey!')

# list_numbers_sum = 0
# for number in number_list:
#     list_numbers_sum = list_numbers_sum + number
# print(list_numbers_sum)

# greeting = 'Hello Python!'
# for letter in greeting:
#     print(letter)

# greeting = 'Hello Python!'
# for letter in greeting:
#     if letter != 'o':
#         print(letter)

# for letter in 'Hello Python!':
#     if letter != 'o':
#         print(letter)

# for letter in 'Hello Python!':
#     print('One more letter!')

# tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# for item in tuple_list:
#     print(item)
# for letter_1, letter_2 in tuple_list:
#     print(letter_1, letter_2)
# for letter_1, letter_2 in tuple_list:
#     print(letter_1)

# tuple_list_1 = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
# for letter_1, letter_2, number in tuple_list_1:
#     print(letter_1, letter_2, number)

# dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#
# # key-value pairs in tuples
# for item in dictionary.items():
#     print(item)
#
# # keys
# for item in dictionary:
#     print(item)
# for item in dictionary.keys():
#     print(item)
# for key, value in dictionary.items():
#     print(key)
#
# # values
# for item in dictionary.values():
#     print(item)
# for key, value in dictionary.items():
#     print(value)

for _ in range(5):
    print('Hello!')


# Part - 4
# Lesson - 27

# while