# # # # # # # # операкоры сраынения
# # # # # # # #  uslovnye operatory
# # # # # # # #  logicheskie operatory


# # # # # # # #  operatory cravneniya

# # # # # # # #  <, >, ==, <=, >=, !=(ne ravno)

# # # # # # # a = 15
# # # # # # # b=15
# # # # # # # result=a==b
# # # # # # # print(result)

# # # # # # a = 23
# # # # # # b=4
# # # # # # print(a!=b)

# # # # # atr='h'
# # # # # str2='a'
# # # # # print(atr>str2)
# # # # # print(ord(atr))

# # # # a='hello'
# # # # b='lesson'
# # # # print(a>b)
# # # # print(ord(b))

# # # *bool --- true(1) or false(0)*


# # # print(chr(104))

# # from multiprocessing import Condition


# # **************************************************

# # # uslovnye operatory

# # # if, elif, else

# # if condition - 
# # esli v if prihodit true
# # <body if>


# # elif if Condition

# # esli true prihodit v uslovie

# # else: 
# #     <body>


# a=input('enter smth')
# if a == 'hello':
#     print('hello world')
# elif a=='mersedes':
#     print('mersdes class s')
# else:
#     print('no sovpadeniy')

# print('code stoped')

# ***


# sign up

# email=input('enter ur e-mAIL:')
# password1=input('enter ur password:')
# password2=input('enter ur password one more time:')
# if password1!=password2:
#     raise Exception('password dont match')
# else:
#     print('u managed to sign up our web')

# ***


# age=input('enter ur age:')
# if age.isdigit():
#     age = int(age)
# else:
#     print('enter correct inf:')
#     raise Exception('value error')
# if age<18:
#     print('dude come in {18 - age} years')
# else:
#     print('u r able to enter')




# ***********************************88

# from operator import ilshift


# logicheskie operatory

# and logicheskaya 
# or lod ilshift
# not log otricanie

# my_age=20
# ur_age=18
# result = my_age ==20 and ur_age==19
# print(result)

# result=my_age>18 or ur_age==20
# print(result)

# result=not my_age != 20
# print(result)
# 8***************8

# from operator 


# is_user_google_user=True
# is_user_github_user=False
# is_user_age_greater_21=False
# user_accounts_coins=2000
# if is_user_google_user and is_user_github_user and (is_user_age_greater_21 or user_accounts_coins>5000):
#     print('u can enter the system mr john smith')
# else:
#     print('u should have google and github account' )

count = 0
num=input()
if num.isdidgit



