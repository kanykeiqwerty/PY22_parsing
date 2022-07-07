# a=list(range(0, 200, 2))
# print(a)

# a=list(range(0, 200))
# ls=[x for x in range(0, 200) if x%2==0 and x%3==0]
# print(ls)
# b=[]
# for i in a:
#     if i%2==0 and i%3==0:
#         b.append(i)

# a=[]
# ls=[x**2 if x%2==0 else x for x in range(0, 100)  ]
# print(ls)

# for i in range(0, 100):
#     if i%2==0:
#         a.append(i**2)
#     else:
#         a.append(i)
        




# *********************************88        #  


# list comprehenssions -> генераторы списка

# newlist = [expression for item in iterable<if condition--True>]

# list comprehession - это упрощенный подход к созданию списка.Который задействует цикл for ,а также конструкции if else
# для определения того, что в итоге окажется добавлено в наш список

# ls=[]
# for i in range(0, 100, 2):
#     ls.append(i)
# print(ls)
# newls=[i for i in range(0, 100, 2)]
# print(newls)

# ls=[i**2 for i in range(0, 11)]
# print(ls)

fruits=['apple', 'banana', 'kiwi', 'mango', 'limon']
# ls=[x.capitalize() for x in fruits]
# print(ls)

# ls=[x for x in fruits if 'a' in x]
# print(ls)

# ls =[x for x in fruits if x!='apple']
# print(ls)

# list_=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ls=[x for inner_list in list_ for x in inner_list ]
# print(ls)


# import datetime
# start=datetime.datetime.now()
# ls=[x for x in range(1, 10000000)]
# ls=[]
# for x in range(1, 100000000):
#     ls.append(x)
# finish=datetime.datetime.now()
# print(finish-start)

# ls=[x+10 if x==8 else x+1 for x in range(0, 10)]
# print(ls)

# c={}


# while True:
#     key_=input('введите ключ:')
#     value_=int(input('введите значение:'))
#     c[key_]=value_
#     if key_=='stop' and value_=='stop':
#         continue
#     b={key_:value_ for key_, value_ in c.items}
#     print(b)

c={s for s in [1, 2, 1, 0]}
print(c)


