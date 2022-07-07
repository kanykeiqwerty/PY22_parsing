# dict() -словарь-> это упорядоченная коллекция элементов(python 3.7-> ordered). Каждый элемент в словаре содержится в паре ключ:значение.

# Ключи должны быть уникальными и быть неизменяемым типом данных(str, int, tuple etc).

# Тогда как значениями могут выступать любые типы данных.

# thisdict={
#     'brand': 'Ford',
#     'model': 'mustang', 
#     'yesr': 1964
# }
# print(thisdict)
# print(type(thisdict))

# hash tables, ассоциативный массив, dictionary, objects(js) -- dictionary(py)
# a={1, 2, 3} #set
# some_tuple=1, 2, 3
# print(type(some_tuple))
# print(some_tuple)

# some_dict = {}
# print(type(some_dict))
# key_values= {'key': 'value', 'key1':'value1'}
# print(type(key_values))
# dict_created_with_function= dict()
# print(type(dict_created_with_function))

# dict_=dict((('key', 'value'), ('key1', 'value1')))
# print(dict_)
# print(type(dict_))


#**********************************************************8




# user_info={
#     'first name': 'john', 
#     'last name': 'snow', 
#     'age': 24,
#     'email': 'johnsnow24@gmail.com', 
#     'list':[1, 2, 3], 
#     'role': 'moderator'}
    # 'first name': 'Raychel'}
# print(user_info['first name'])
# print(user_info.get('age'))
# print(dir(dict))


# print(user_info.items())
# for items in user_info.items():
#     print(items)


# print(user_info.keys()) #before changes


# user_info['age']=30
# print(user_info.keys()) # after changes
# print(user_info)

# for key in user_info.keys():
#     print(key)

# for value in user_info.values():
#     print(value)


# pop() удаляет элемент по выделенному ключу

# popitem() удаляет последнюю пару(элемент) в dict

# print(user_info)
# user_info.pop('list')
# user_info.pop('email')
# user_info.popitem()
# user_info.popitem()
# print(user_info)

# setdefault(key, [default value]) работает так же как и мето get(), но если такого ключа не существует, он создаст новую пароу значений.

# 1 способ применения, получение значений
# dict_ ={'name': 'john', 'age': 23}
# result=dict_.setdefault('age')
# print(result)

#2 способ применения, добавление пары
# dict_ ={'name': 'john', 'age': 23}
# result=dict_.setdefault('address')
# print(dict_)


# print(user_info)
# user_info.update({'first name': 'Raychel'})
# user_info.update({'height': 185})
# print(user_info)

# user_info['first name']='Raychel'
# user_info['height']=185
# print(user_info)


# # **********************************************************

# roles={
#     0: 'admin',
#     1: 'Moderator',
#     2: 'Vendor',
#     3: 'customer',
#     4: 'guest'
    
# }

# users=[
#     {'id': 0,
#     'name': 'john',
#     'role': roles[0]
#     }, {'id': 1,
#     'name': 'Raychel',
#     'role': roles[3]},
#     {'id': 2,
#     'name': 'Aibek',
#     'role': roles[4]},
# ]

# product={
#     'id':1,
#     'title': 'samsung galaxy s20',
#     'discription': 'lorem ipsum',
#     'price': 1000
    
# }
# print(users)
# print(product)
# user_id=int(input('enter your id'))
# if users[user_id]['role']==roles[0]:
#     product['discription']=input('enter new product name:')
# else:
#     raise Exception('u dont have enough righns')
# # print(product)
# import random
# ls=['Plov', 'Manty', 'Kuurdak', 'Lagman', 'dymdama']
# p=0
# m=0
# k=0
# l=0
# d=0
# for i in range(0, 100000):
#     choice=random.choice(ls)
#     print(choice)
#     if choice.lower()=='plov':
#         p=p+1 #mp+=1 инкримент
#     elif choice.lower()=='manty':
#         m=m+1
#     elif choice.lower()=='kuurdak':
#         k+=1
#     elif choice.lower()=='lagman':
#         l+=1
#     elif choice.lower()=='dymdama':
#         d+=1
# # print(f'plov: {p},\nManty: {m},\nKuurdak: {k},\nLagman: {l}')
# # if p>m and p>k and p>l:
# #     print
# print(f'по

# dict_={'plow':p, 'Manty':m, 'Kuurdak':k, 'lagman': l, 'dymdama':d}
# # print(dict_)
# # result=sorted(dict_.items(), key=lambda x: x[1]) #1way
# # def func(x:tuple):#2 way
# #     return x[1]
# result=sorted(dict_.items(), key=func)
# winner=result[-1]бедила блюдо: {winner[0]}, оно набрало:{winner[1]} ')
# # вывести победителя




        
       



    
