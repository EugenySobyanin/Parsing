""" Выполнение программы в одном потоке."""

# from datetime import datetime

# import requests

# # Функция с расчётом среднего арифметического.
# def task(number):
#     result = 0
#     value = number ** number

#     for i in range(1, value + 1):
#         result += i
#         if i % 1000000 == 0:
#             # Вот он GET-запрос.
#             requests.get('https://python.org')
#     return result / value

# if __name__ == '__main__':
#     print('Начало работы основного потока')
#     # Фиксируется время начала выполнения программы.
#     start_time = datetime.now()
#     print(task(8))
#     print(task(8))
#     # Фиксируется время окончания выполнения программы.
#     end_time = datetime.now()

#     print('Окончание работы основного потока')
#     print(f'Итоговое время выполнения: {end_time - start_time} секунд.')


"""Выполнение в разных потоках."""
# import threading
# from datetime import datetime

# import requests


# def task(number):
#     result = 0
#     value = number ** number

#     for i in range(1, value + 1):
#         result += i
#         if i % 1000000 == 0:
#             # Вот он GET-запрос.
#             requests.get('https://python.org')
#     print('Среднее арифметическое равно:', result / value)

# if __name__ == '__main__':
#     print('Начало работы основного потока')

#     start_time = datetime.now()
#     # При создании экземпляра класса Tread указывается два параметра: 
#     # target — название функции,
#     # args — аргумент для этой функции, в нашем случае это значение n.
#     # Кортеж из одного элемента должен заканчиваться запятой.
#     t1 = threading.Thread(target=task, args=(8,))
#     t2 = threading.Thread(target=task, args=(8,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     end_time = datetime.now()

#     print('Окончание работы основного потока')
#     print(f'Итоговое время выполнения: {end_time - start_time} секунд.')


"""Выполняется в разных процессах."""
import multiprocessing
from datetime import datetime

import requests


def task(number):
    result = 0
    value = number ** number

    for i in range(1, value + 1):
        result += i
        if i % 1000000 == 0:
            # Вот он GET-запрос.
            requests.get('https://python.org')
    print('Среднее арифметическое равно:', result / value)

if __name__ == '__main__':
    print('Начало работы основного потока')

    start_time = datetime.now()
    t1 = multiprocessing.Process(target=task, args=(8,))
    t2 = multiprocessing.Process(target=task, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = datetime.now()

    print('Окончание работы основного потока')
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')