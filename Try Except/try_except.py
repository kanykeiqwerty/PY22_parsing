# обработка исключений 
# операторы try and except

# ошибки: связанные с кодом
#SyntaxError
# IndentationError
# TabError

# исключения - это нерабочие данные
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException прародитель всех ошибок

# try except
# try:
#     body try>
# except:
#     bode except>


# num1=int(input('enter the num:'))
# print(num1)
# print('very import strok')

# try:
#     num1=int(input('enter the num:'))
#     print(num1)
# except:
#     print('you entered uncorrect value')
# print('very important strok')

#1 import sys
# list_=[1, 2, 3, 4, 5]
# index=int(input('enter index:'))
# try:
#     res =list_[index]
#     print(res)
# except :
#     import sys
#     print('oops, we cathed {sys.exc_info()[0} error')


#2 Exception as e
# list_=[1, 2, 3, 4, 5]
# index=int(input('enter index:'))
# try:
#     res =list_[index]
#     print(res)
# except Exception as e:
#     print(f'oops, we cathed {e.__class__} error')

# list_=[1, 2, 3, 4, 5]

# try:
#     index=int(input('enter index:'))
#     res =list_[index]
#     print(res)
# except IndexError:
#     print('you entered uncorrected index ')
# except ValueError:
#     print('you entered uncorrected value ')


# else в try  except 
# finally in try   except



# try:
#     body
# except:
#     body
# else:
#     body сработает если в операторе try не случилась ошибка
# finally:
#     body сработает при любом исходе


# try:
#     num1=int(input())
#     num2=int(input())
#     r=num1/num2
# except ZeroDivisionError:
#     print('на ноль делить нельзя')
# except ValueError:
#     print('invalid symbols')
# else:
    
#     print(r)
# finally:
#     print('code finished')




# try:
#     b=10
#     c=11
#     print(a)
# except NameError:
#     print(' такого значения нет')

# try:
#   a=int(input())
#   b=int(input())
#   c=a/b
#   print(c)
# except ZeroDivisionError:
#   print('на ноль делить нельзя')
    
# try:
#   a=int(input())
#   b=int(input())
#   c=a+b
#   print(c)
# except ValueError:
#   print('введите целое число')



# a= {}
# try:
#    print(a['username'])
# except KeyError:
#    print('такого ключа нет')

# try:
#   a=input().split()
#   i=int(input('index'))
#   print(a[i])
# except IndexError:
#   print('такого элемента нет')

# try:
#   a=int(input())
#   b=int(input())
#   print(a/b)
# except ValueError:
#   print('введите целое число')
# except ZeroDivisionError:
#   print('на ноль делить нельзя')


# try:
#     money = int(input())
#     if money < 0: raise
# except:
#     print('Сумма не может быть отрицательной!')


# try:
#   age=int(input('your age'))
 
#   if age<18:
#     raise PermissionError('Access is denied')
# except ValueError:
#   print('Incorrect age entered')
# else:
#   print('thank you')
# finally:
#   print('good bye')

# try:
#   a=input()
#   b=input()
#   print(int(a)+int(b))
# except ValueError:
#   print(a+b)

# try:
#   a=input().split()
#   b=[int(x) for x in a ]
#   print(b)
  
# except :
#   print('Данный элемент не является числом!')

