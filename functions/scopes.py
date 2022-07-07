# области видимости и пространства имен

# Built=in -встроенная облась видимости(print, len, max, int)
# global -глобальная облась видимости
# enclosed(не локальная, nonlocal)
# local(самая маленькая, локальная облась видимости) 


# def printlist(somelist):
#     for i in  somelist:
#         print(i)
# i='q'
# printlist([1, 2, 3])
# print(i)

# a=10 # global
# print #built-in
# def hello():#global
#     a='hello world'#local
#     print(a, 'local inside at func')
# hello()
# print(a, 'global')


# x='glpbal'
# print(x,'1') #1
# def enclosed():
#     x='enclosed'
#     def local():
#         x='local'
#         print(x,'3')#3
#     print(x, '2')#2
#     local()
#     print(x, '4')#4
# enclosed()
# print(x, '5')#5

# var=100 #global
# def increment():
#     # var=var+1 # try to update a global
#     print(var)
# increment()

# global-> позволяет ихменять значения глобальной переменной находясь в локальной области видимости

# nonlocal -позволяет менять значения не локальной переменной находясь в локальной области виидимости
 

# var=100
# def increment():
#     global var
#     var+=1
# print(var)
# increment()
# print(var)

# def counter():
#     num=0
#     def increment():
#         nonlocal num
#         num+=1
#         return num
#     return increment
# c=counter()
# print(c())
# print(c())
# print(c())
# c=counter()
# print(c())

# print(len(dir(__builtins__)))

# print(abs(-15))# стандартный вызов встроенной функции
# abs=-15#переопределяю встроенное имя abs в глобавльной области
# del abs
# print(abs(-15))

#********************************
# while True:
#     a=input().split()
#     c=[int(i) for i in a]
#     continue

# a=[[1, 2, 3], [4, 5, 6]]
# b=[sum(i) for i in a]
# print(max(b))

# from importlib.resources import path


# al=[33, 66, 10]
# bl=[33, 66, 10]
# def sd(a, b):
#     scorea=0
#     scoreb=0
#     for i in range(0, len(a)):
#         if a[1]>b[i]:
#             scorea+=1
#         elif b[1]>a[1]:
#             scoreb+=1
#         else:
#             path
#         return{'Alica': scorea, 'john': scoreb}
# print(sd(al, bl))
# print(sd([34, 20, 10], [10, 35, 5]))


# a = 'pythonist'
# my_dict = {i: a.count(i) for i in a}
# print(my_dict)






