# Импорт модуля для работы с процессами.
import multiprocessing
from time import sleep

# Эта функция будет работать в первом процессе.
def task_1():
    print('Процесс 1 начал работу')
    a = 2
    b = 3
    result = a + b
    print(result)
    for i in range(1, 4): 
        print(f'Инструкция {i} из процесса 1') 
        sleep(1)

    print('Процесс 1 завершил работу')

# Эта функция будет работать во втором процессе.
def task_2():
    print('Процесс 2 начал работу')
    text = 'Строчка, которая гуляет сама по себе'
    print(text)
    for i in range(1, 4): 
        print(f'Инструкция {i} из процесса 2') 
        sleep(1)

    print('Процесс 2 завершил работу')

# Основной поток.
if __name__ == '__main__':
    
    print('Начало работы основного потока')
    
    # Тут создаются процессы.
    t1 = multiprocessing.Process(target=task_1)
    t2 = multiprocessing.Process(target=task_2)
    
    # Тут процессы запускаются.
    t1.start()
    t2.start()
    
    # Пока все процессы не закончат работу, не продолжат выполняться 
    # инструкции из основного потока.
    t1.join()
    t2.join()

    print('Окончание работы основного потока')