# Part - 4
# Lesson - 18

# Lists

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
# удаляет по значению, но удаляет только попавшийся элемент
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
