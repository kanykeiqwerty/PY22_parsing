# def sumofargs(a:int, b:int, c:int, d:int)->int:#a, b, c, d->параметры
#     """
#     returns of all parametrs
#     """
#     return a+b+c+d
# r=sumofargs
# print(r(5, 4, 4, 6))




#*****************88
# позицонные и именованные аргументы

# def printparams(a, b=None, c=None):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')
# printparams(c=3, a=5)

# from string import digits


# def sumofargs(a:int, b:int, c:int, d:int)->int:#a, b, c, d->параметры
#     """
#     returns of all parametrs
#     """
#     return a+b+c+d
# print(sumofargs(1, 2, 3, 4)) #ПОЗИЦИОННЫЕ АРГУМЕНТЫ(arguments)
# print(sumofargs(a=5,b= 6, d=7, c=6))#именованные аргументы(keyword arguments)
# print(sumofargs(5, 10 ,c=20, d=15))

#********************************************
# оперфтор * 
# a=[1, 2, 3]
# b=[4, 5, 6]
# c=[*a, *b]
# print(c)
# print(*a, end='*')


#*****************88888
# *args **kwargs в фуnкциях
# def printscores(a, *args):
#     print(f'gh name:{a}')
#     print(args)
#     print(type(args))
#     for x in args:
#         print(f'mark:', x)

# printscores('john snow', 100, 88, 80, 70, 96)

# def printpetnames(owner, **kwargs):
#     print(f'owner name:{owner}')
#     print(print(kwargs))
#     print(type(kwargs))
#     for pet, name in kwargs.items():
#         print(f'{pet}:{name}')
# printpetnames('john snow', dog='rex', cat='larry', fish=['nemo', 'dori', 'alex'], turtle='leonardo')

# def getsomedata(a, b, *args, **kwargs):
#     print('параметры a and b:', a, b)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])
#     print('arguments', args)
#     print('именованные аргументы', kwargs)
# getsomedata(1, 2, 3, 4, 5, lang='python', name='john snow', car='bmww ms')

#*************************8
# def cone2strings(str1, str2):
#     import random
#     res=random.randint(1, 10)
#     return str1+str2+str(res)
# result=cone2strings('hello', 'world')
# print(result)


#**************************************8


# def generatepassword(name, fam):
#     import random
#     randomnum=random.randint(100000, 999999)
#     return name + fam + '_'+str(randomnum)
# def getinfo():
#     name=input()
#     fam=input()
#     return generatepassword(name, fam)
# result=getinfo()
# # print(result)
# %***************************************
# def generaterandomstr(len_, lang):
#     import random
#     import string as s
#     randomstr=''.join(random.choice(s.ascii_lowercase + s.digits) for i in range(0, len_))
#     return randomstr
# print(generaterandomstr(15, 'eng'))

#**********************************
# def add(num1, num2): return num1 + num2
# def subtract(num1, num2): return num1-num2
# def multiply(num1, num2): return num1*num2
# def divide(num1, num2):
#     try:
#         return num1/num2
#     except ZeroDivisionError:
#         return 'na nol delit nelzya'
# def main():
#     try:
#         num1=float(input())
#         num2=float(input())
#     except ValueError:
#         print('u entered incorrect value')
#         main()
#     operator=input('vvedite operator(+, -, /, *):')
#     result=None
#     if operator=='+': result=add(num1, num2)
#     elif operator=='-':result=subtract(num1, num2)
#     elif operator=='*': result=multiply(num1, num2)
#     elif operator=='/': result=divide(num1, num2)
#     else:
#         print('u entered incorrect operator')
#     operator()
#     print(f'result:{result}')
#     question=input('do u wanna continue&(yes or no')
#     if question.lower()=='yes':
#         main()
#     else:
#         print('thanks for using ur calculator, bye!')
# main()




