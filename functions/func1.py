# def <name of fuction>(<a, b>- праметры):
#     <body> некая логика, код
#     <return>возвращаем что то
# <name of fuction>(<5, 6 # аргументы>)


# gпартметры функции - перменные которые будет принимать
#   наша функция для того чтобы, мы смогли работать с данными которые передаются в эту функцию

# аргументы -данные которые мы передаем для параметров при вызове функции
# return нужен для того чтобы функция что то возвращала и для того 
# чтобы мы могли работать с результатом действия функции. return является необязательным операторoм
# (возвращает None если не указать return)

# ls=[]
# print(ls.append(1))
# print(ls)

# print(ls.pop())





# def sumTwoNums(a, b): # парамаетры
#     c=a+b
#     print(c)
#     return c
# print(sumTwoNums(5, 5))

# def iseven(a):
#     if a%2==0:
#         return True
#     else:
#         return False
# print(iseven(5))
# a=10
# b=int(input())
# print(iseven(a))
# print(iseven(b))


# def iseven(a: int)->bool:
#     """
#     нашафункция проверяет является ли функция типа инт четным .
#     """
#     if a%2==0:
#        return True
#     return False
# iseven
# from typing import List

# def getpolindrom(words: List(str)) -> list:
#     """
#     Функция возвращает список из полиндромов
#     """
#     r=[]
#     for word in words:
#         if word.lower()==word[::-1].lower():
#             r.append(word)
#     return r
# somewords=['john', 'kazak', 'parker', 'anna', 'dovod', 'food', 'water']
# print(getpolindrom(somewords))


#****************************8

#default params
# def printwelcome(name: str='user')->str:
#     print(f'welcome, {name}')
# printwelcome('kanykei')


from logging import raiseExceptions


# def getpercentage(a:float, period: int)->float:
#     """
#     return final amount of money
#     """
#     if a<30000:
#         raise Exception('вы ввели некорректное количество денег, мин ставка 30000сом')
#     if period<3:
#         raise Exception('вы ввели некорректный срок для депозита, минимальный срок 3 года')
#     i=0
#     while i<period:
#         a=a+(a*0.1)        
#         i+=1
#     return a
# a=float(input())
# period=int(input())
# print(getpercentage(a, period))



# def getreverse(a: str)->str:
#     s=a.split(' ')[::-1]
#     r=' '.join(s)
#     return r
# print(getreverse('Hello world!My nae is John, last is Snow. Nice to meet you'))
    

# def gettype(a, b):
#   c=type(a)
#   d=type(b)
#   return c, d
# a=input()
# b=input()
# print(gettype(a, b))


# def getdivision(a, b):
#   c=a/b
#   return c
# a=int(input())
# b=int(input())
# print(getdivision(a, b))

# def getkeys(a:dict)->list:
#   b=[x for x in a.keys()]
#   return b
# while True:
#     key=input().split()
#     val=input().split()
#     a={x:y for x in key for y in val}
#     break
# print(getkeys(a))

# def getmultiplication(a:list)->int:
#     b=1
#     for i in a:
#        b*=int(i)
#     return b
# a=input().split()
# print(getmultiplication(a))



# def getsum(a:int)->int:
#     b=[int(x) for x in str(a)]
#     return b
# a=int(input())
# print(getsum(a))

# def gernum(a):
#   if a%2==0:
#     print('it is even num')
#   else:
#     print('it is odd num')
# a=int(input())
# print(gernum(a))

# def getmax(a, b):
#   c=max(a, b)
#   return c
# a=int(input())
# b=int(input())
# print(getmax(a, b))

# def getpolindrom(word: (str)) -> str:
#    if word.lower()==word[::-1].lower():
#      return True
#    else:
#      return False
# word=input()
# print(getpolindrom(word))

# def getlist(a, b):
#   b=list(range(a, b, 2))
#   return b
# a=int(input())
# b=int(input())
# print(getlist(a, b))

# def test(lst):
#     return len(lst)==10 and lst.count('с')==lst.count('ю') and lst.count('з')==lst.count('в')






    

   
    

        




