#СТЕК - #По идее ответ должен быть от 5 до 1 но в СТЕКЕ всё наборот от последнего до первого
def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print(n)
p(5)



#Программа для проверки корректности скобок
def par_checker(string): #string это будет наше вводное значение
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем её в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент — открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит, возвращаем True, иначе — False
    return len(stack) == 0
print(par_checker('(5+6)*(7+8)/(4+3)'))

#Меняем программу и добавляем туда проверку еще и квадратных скобок
#Создадим словарь где правая скобка - ключ, а левая - значение
pars = {")": "(", "]": "["}
def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
print(par_checker_mod('[]'))


#Обработчик задач на бесконечном цикле с использованием очереди
N_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(N_max)]
order = 0
head = 0
tail = 0

def is_empty():
    return head == tail and queue[head] == 0

def size():
    if is_empty():
        return 0
    elif head == tail:
        return N_max
    elif head > tail:
        return N_max - head + tail
    else:
        return tail - head

def add():
    global tail, order
    order += 1
    queue[tail] = order
    print("Задача №%d добавлена" % (queue[tail]))
    tail = (tail + 1) % N_max

def show():
    global head
    print("Задача №%d в приоритете" % (queue[head]))

def do():
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0
    head = (head + 1) % N_max

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")



#РАЗБЕРЕМ ВСЮ ПРОГРАММУ ПО ЧАСТЯМ
#Функция is_empty, проверяющая наличие элементов в очереди, используя указатели head и tail
def is_empty(): # очередь пуста?
    # да, если указатели совпадают и в них содержится ноль
    return head == tail and queue[head] == 0


#Функция проверяет текущий размер очереди
def size(): # получаем размер очереди
    if is_empty(): # если она пуста
        return 0 # возвращаем ноль
    elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
        return N_max # значит очередь заполнена
    elif head > tail: # если хвост очереди сместился в начало списка(закольцевался)
        return N_max - head + tail
    else: # или если хвост стоит правее начала
        return tail - head


#Функция добавляющая задачу в конец очереди
def add():  # добавляем задачу в очередь
    global tail, order
    order += 1  # увеличиваем порядковый номер задачи
    queue[tail] = order  # добавляем его в очередь
    print("Задача №%d добавлена" % (queue[tail]))

    tail = (tail + 1) % N_max
    # увеличиваем указатель на 1 по модулю максимального числа элементов
    # для зацикливания очереди в списке


#Вывести в приоритет задачу
def show(): # выводим приоритетную задачу
    print("Задача №%d в приоритете" % (queue[head]))


#Функиця выполняет задачу, удаляет её из очереди присваивая значение 0
def do(): # выполняем приоритетную задачу
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0 # после выполнения зануляем элемент по указателю
    head = (head + 1) % N_max # и циклично перемещаем указатель