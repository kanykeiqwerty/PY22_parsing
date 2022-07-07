#list()( список или массив) - изменяемый, последовательный тип данных, который из себя представляет коллекцию каких-либо объектов. 

# my_list=[1, 'string', False, None, [1, 2, 3]]
# print(my_list)
# print(type(my_list))


# 1. list(<iterable>)
# my_list=list('hello world')
# print(my_list)
# tuple=('banana', 'cherry', 'apple')
# print(tuple)
# print(type(tuple))
# my_list=list(tuple)
# print(my_list)
# print(type(my_list))



#2.range() возвращает последовательность элементов(числа)

# a=list(range(1, 100, 2))
# print(a)


# 3. []

# a=[1, 2, 3, 4, 4 ]
# print(type(a))
# print(a)


# 888****************************************
# print(dir(list))

# append(element) добавляет элемент в конец списка

# a=[1, 2, 3]
# print(a)
# a.append(5)
# a.append([1, 2, 3])
# print(a)

# extend(element[interable]) расширяет список добавляя элемент в конец

# a=[1, 2, 3]
# a.extend('hello')
# print(a)

# insert(< index>, <element>) добавляет элемент по указанному индексу

# a=['string', 2, 3, False]
# a.insert(1, [1, 2, 3, None])
# a.insert(2, 1)
# print(a)
# print(a[-1])
# print(a[1][3])
# print(a[2:5])

# print(len(a))


#index(<element, [start], [end]>) возвращает  индекс элемента

# a=[1, 2, 3, 33, 4, 5, 5, 7, 2, 'hello']
# print(a.index(5, 6))
# if 'hello' in a:
#     print(f'"hello" is in a:{a.index("hello")}')
#     print(f'"hello" is in a:', a.index('hello'))


# count(element)возвращает количество вхождений элементов в списке

# a=[1, 2, 3, 4, 5, 5, 5, 5, 1]
# print(a.count())


#remove(element) удаляет элемент, но если такого элемента нет в списке, то выводит ошибку

# pop(index) удаляет и возвращает элемент по индексу, но если индекс не указна, то удаляет последний элемент 

# a=[5, 1, 2, 3, 4, 5]
# a.remove(5)
# a.remove(5)
# a.pop()
# a.pop(0)
# d=a.remove(4)
# print(a)
# print(d)

#sort(reverse=tru or false, key=<>) сортирует список. если в документах указан reverse = true, то список будет отсортирован в убывающем порядке.

# a= [5, 0, -2, -101, 102,103, 23, 1]
# print(a)
# a.sort() по  ыозрастанию
# a.sort(reverse=True) по убыванию
# print(a)


# a=['hello', 'london', 'a']
# a.sort(key=len, reverse=True)
# print(a)

# a=[1, 'h', 3]
# a[1]=2         #изменение списка
# print(a)

# del a[-1]
# print(a)

# import random
# import math
# a=list(range(9))
# a=random.sample(a, 3)
# b=list(range(9))
# b=random.sample(a, 3)
# c=a+b
# d=math.fsum(list(map(int, c)))
# print(c, d)

# a=str(input())
# if len(a)&2==0:
#     b=len(a)/2 
#     c=len(a)/2
#     print(a[b:] + a[:b])
# elif len(a)&2>0:
#     c=len(a)//2
#     b=a-c
#     print(a[b:] + a[:b])







