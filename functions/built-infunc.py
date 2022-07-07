# встроенные функции

# print()...

# map()
# filter()
# lambda()
# enumerate()

# анонимные функции- lambda(это такие же функции, только без названия)
#\ lambda функции могут примимать сколько угодно аргументов,
# \ но всегда возвращает только одно выражение


# def sumargs(a, b): 
#     result=a+b
#     return result

# def sumargs1(a, b): return a+b
# print(sumargs(1, 2))
# print(sumargs1(1, 2))

# sumarg=lambda a, b: a+b
# print(sumarg(1, 2))



# x=lambda a, b, c:a+b+c
# print(x(5, 6 ,7))

# def myfunc(n):
#     return lambda a:a*n
# mydoubler=myfunc(2)
# mytripler=myfunc(3)
# print(mydoubler(11))
# print(mydoubler(22))
# print(mytripler(11))
# print(mytripler(22))




# ls=['def', 'ivan', 'john', '', ' ']
# newls=sorted(ls, key=len)
# print(newls)


#***************************

# map(function, iterable)->применяет функцию к каждому элементу последовательности 
# и возвращает mapobject(итератор) с результатами

# например, с помощью map можно выполнять преобразования элементов.
#  Перевести все строки в верхний регистр:
# listofwords=['one', 'two', 'three', 'dict']
# result=list(map(str.upper, listofwords))
# print(result)
# result2=list(map(len, listofwords))
# print(result2)

# ls=['1', '2', '3', '4']
# result=list(map(int, ls))
# print(result)

# names=['john', 'jemmy', 'sansa', 'tirion', 'aibek']

# result=list(map(lambda x: f'hello mr/mrs {x}', names))
# print(result)

# nums=[1, 2, 3, 4, 5]
# nums2=[100, 200, 300, 400, 500]
# result=list(map(lambda x, y:x*y, nums, nums2))
# print(result)


# dict_={1:2, 3:4, 5:6}
# result=dict(map(lambda items:(items[0], str(items[1])), dict_.items()))
# print(result)


#******************************************************************************

# filter(function, iterable) -применяет функцию ко всем элементам последовательности (iterable object)
# функцию которую мы передаем и возвращает filterobject(итератор) 
# с теми объектами для которых функция вернула TRue


# ls=['one', 'two', 'list', '', '100', '1', '50', 'john99']
# result=filter(str.isdigit, ls)
# print(list(result))
# for x in result:
#     print(x)

# ls=[10, 11, 102, 213, 314, 515]
# result=filter(lambda x:x%2!=0, ls)
# print(list(result))


# ls=['john', 'one', 'two', 'list', 'makers', 'ev22', 'ono']
# result=filter(lambda x:len(x)>=4, ls)
# print(list(result))

name='sandy'
def func():
    name='andy'
    def func2():
        name='mandy'
        print(name)
        print(locals())
    func2()
func()


#***********************************************************
# enumerate(iterable)- 

# ls=['str1', 'str2', 'str3']
# i=0
# for x in ls:
#     print(f'el:{x}, in:{i}')
#     i+=1

# for i, x in enumerate(ls):
#     print(f'el:{x}, in:{i}')

# newls=list(enumerate(ls))
# print(newls)
























