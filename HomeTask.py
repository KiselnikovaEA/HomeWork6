# ДЗ 5, Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open('Task1_text.txt', 'r', encoding='utf-8') as f:
#     data = f.read()
#     print('Исходный текст: ', data)

# words = data.split()

# new_text = " ".join(list(filter(lambda x: 'абв' not in x, words))) # использование функции filter() и lambda
# print('Преобразованный текст: ', new_text)

# with open ('Task1_new_text.txt', 'w', encoding='utf-8') as new_file:
#     new_file.write(new_text)

# ДЗ 4, Задача 3, Вариант б): список уникальных неповторяющихся элементов [1, 1, 2, 2, 3, 5] -----> [3,5]
# Удалось сократить кол-во строк кода с 10 до 3-х

# some_list = list(map(int, input().split())) # использование map()
# unique_values = [i for i in some_lst if i.count == 1]  # Использование list comprehension
# print(unique_values)

# enumerate() можно было использовать в задаче, где составляли многочлен для записи в файл,
# но у меня несколько другая реализация, не подойдёт, т.к. я не успользовала в цикле лист с коеффициентами полностью
# Так же как и в других задачах я не встретила пробежку по списку ровно от начала до конца

# Задач, подходящих для использования функции zip() не встречалось