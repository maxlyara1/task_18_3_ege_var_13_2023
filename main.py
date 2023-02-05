import random

# Создаю лист из значений, которые используются в задании
x = [2, 3, 4, 5, 6, 16]

i = 0
min_value = 10000
list_of_possible_answers = []
lists_in_list_counter = 0

while True:
    # Создаю лист с рандомными значениями из листа начальных значений, с помощью которых будет осуществлен
    # перебор на каждой итерации
    x = random.sample(x, 6)

    # Собственно сами вычисления
    temp = x[0] / x[1] + x[2] / x[3] + x[4] / x[5]

    # Сравнение
    if min_value > temp:
        min_value = temp
        min_x = x
        # print('temp -', temp)
        # print('values in order', min_x)
        # print(i)

    #Это я уже создал, когда знал минимальное значение, чтобы получить лист из комбинаций значений для ответов
    if temp == 1.15 and x not in list_of_possible_answers:
        list_of_possible_answers.append(x)
        lists_in_list_counter += 1

    # Если минимальное значение не изменилось, то увеличиваю коэффицент необходимости повторения цикла
    # Или уменьшаю его до 0, чтобы точность была высокой
    if min_value < temp:
        i += 1
    else:
        i = 0
    if i > 1000:
        break

# Вывод
print('min_value:', min_value)
# print('values in order', min_x)
print('list_of_possible_answers:', list_of_possible_answers)
print('lists_in_list_counted:', lists_in_list_counter)

# Ответ
# min_value: 1.15
# list_of_possible_answers: [[4, 16, 3, 6, 2, 5], [4, 16, 2, 5, 3, 6], [2, 5, 3, 6, 4, 16], [3, 6, 4, 16, 2, 5],
# [2, 5, 4, 16, 3, 6], [3, 6, 2, 5, 4, 16]]
# lists_in_list_counted: 6
