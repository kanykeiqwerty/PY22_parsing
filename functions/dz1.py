# 1. Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
# """
# def getsum(a, b):
#   c=a+b
#   return c
# a=int(input())
# b=int(input())
# print(getsum(a, b))

# """
# 2. Создайте функцию, которая будет принимать строку. Функция должна выводить длину этой строки.
# """

# def getlen(a:str)->int:
#   c=len(a)
#   return c
# a=input()
# print(getlen(a))


# """
# 3. Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип данных принятых аргументов.
# """

# def gettype(a, b):
#   c=type(a, b)
#   return c
# a=input()
# b=input()
# print(gettype(a, b))


# """
# 4. Создайте функцию, которая должна принимать 2 числа и возвращать результат их деления.
# """

# def getdivision(a, b):
#   c=a/b
#   return c
# a=int(input())
# b=int(input())
# print(getdivision(a, b))

# """

# """

# """
# 5. Создайте функцию, которая принимает словарь. Пройдитесь по словарю циклом и распечатайте все его ключи
# """

# def getkeys(a:dict)->list:
#   b=[x for x in a.keys()]
#   return b
# while True:
#     key=input().split()
#     val=input().split()
#     a={x:y for x in key for y in val}
#     break
# print(getkeys(a))
# print(type(a))

  
  
    


# """
# 6. Напишите функцию, которая принимает список чисел и возвращает их произведение.
# """

# def getmultiplication(a:list)->int:
#     b=1
#     for i in a:
#        b*=int(i)
    # return b
# a=input().split()
# print(getmultiplication(a))


# """
# 7. Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр.
# """

# def getsum(a:int)->int:
#     b=[int(x) for x in str(a)]
#     return b
# a=int(input())
# print(getsum(a))
  


# """

# """


# """
# 8. Создайте функцию, которая принимает число и выводит "It's even number" если число четное(делится на 2 без остатка - 2, 4, 20 и.т.п), если же число нечетное (3, 9 и.т.п) функция должна выводить "It's odd number".
# """

# def gernum(a):
#   if a%2==0:
#     print('it is even num')
#   else:
#     print('it is odd num')
# a=int(input())
# print(gernum(a))

# """
# 9. Создайте функцию которая принимает от пользователя два числа. Функция должна сравнить эти числа между собой и вывести максимальное значение.
# """

# def getmax(a, b):
#   c=max(a, b)
#   return c
# a=int(input())
# b=int(input())
# print(getmax(a, b))


# """
# 10. Напишите функцию, которая будет принимать строку и проверять является ли она палиндромом. Пробелы и регистр учитывать не нужно.

# >Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.
# """

# def getpolindrom(word: (str)) -> str:
#    if word.lower()==word[::-1].lower():
#      return True
#    else:
#      return False
# word=input()
# print(getpolindrom(word))



# def foo():
#     var = 'переменная foo'
#     def bar():
#         var = 'переменная bar'
#         print("переменная в foo: ", var)
#     print("переменная в foo: ", var)
#     bar()
# foo()


# x='Я глобальная переменная!'
# def change():
#   global x
#   x='Я могу изменяться'
# print(x)
# change()
# print(x)

# num=3
# def mul():
#   global num
#   num=3**2
# mul()
# print(num)

# balance=0
# def getsalary(amount):
#     global balance
#     balance+=amount
# def pay_bills(amount:int, log_name:str):
#         global balance
#         balance-=amount
#         print(f'Вы запалтили {amount} сом за {log_name}')
# def get_balance():
#     print(f'у вас на счету {balance} сом')        
      
# getsalary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# result=0
# def pow_first(x, y):
#     global result
#     result=x**y
# def pow_second(z):
#         global result
#         result%=z
        
# pow_first(4, 2)
# pow_second(7)
# print(result)
    

# def year(a):
#   for j, i in a.items():
#     if i<=17:
#       print(f'в клуб не прошли:{j}')
#     elif i>17:
#       print(f'в клуб прошли:{j}')

# year({'Murat':24, 'Erjan':21, 'Chyngyz':24, 'Altynai':17, 'asema':16})


# def names(a):
#   b=[x.title() for x in a]
#   print(b)
#   return b
# a=input().split()
# names(a)

# def get(a):
#     g=0
#     s=0
#     other=0
#     for x in a:
#         if x.lower() in 'аеуоияыэю':
#             g+=1
#         elif x.lower() in 'йцкнгшщзхъфвпрлджчсмтьб':
#             s+=1
#         else:
#             other+=1
#     print(f"гласные{g},согласные {s},другие символы {other}")
# a=input()
# get(a)
 

# a=int(input())
# for i in list(range(a)):
#   if i<7:
#     print(i)

# 

# b=int(input())
# a=list(range(b))
# c=list(map(lambda x:x**2, a))
# print(c)


# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# newlist_=list(map(lambda x:x>=0, list_ ))
# print(newlist_)


# a=int(input())
# b=list(filter(lambda x:x%2==0, list(range(a))))
# print(b)


# b=list(filter(lambda x:len(x)>7, input().split()))
# print(b)

# a=int(input())
# b=list(filter(lambda x:x%2==0, list(range(a))))
# c=list(filter(lambda x:x%2!=0, list(range(a))))
# print(f'количество четных чисел:{len(b)},количество нечетных чисел:{ len(c)}')



# def get(b):
#     for i in b:
#         if i>3:
#             return True
#         else:
#             return False
# a=int(input())
# b=list(range(a))
# print(get(b))

# a=int(input())
# b=int(input())
# c=list(map(lambda x:x>3, list(range(a, b))))
# print(c)

# a=int(input())
# b=int(input())
# c=list(map(lambda x:x<0, list(range(a, b))))
# print(c)
# my_list = ['m', 'a', 'k', 'e', 'r', 's']
# import functools

# new_word = functools.reduce(lambda x, y: x + y, my_list)
# print(new_word)

# import functools
# list_ = [1, 2, 3, 4]
# a=functools.reduce(lambda x,y:x+y, list_)
# print(a)

# import functools
# list_ = [1, 2, 3, 4]
# a=functools.reduce(lambda x,y:x*y, list_)
# print(a)


from functools import reduce 
names=input().split()
a = reduce(lambda a, b : a if (len(a) > len(b)) else b, names) 
print(a)



