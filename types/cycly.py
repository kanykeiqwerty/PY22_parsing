# for value in tuple1:
#     print(value)



# names=('Tima', 'zhanylai', 'Aidana', 'bermet', 'Ermak')
# # print(names[0] + ' hello')
# names_enter=['Bermet', 'ermek']
# for name in names:
#     if name.capitalize() in names:
#         print(f'hello {name.capitalize()}')
#     else:
#          print(f'{name} go home')
    # print('it is len:', len(name))
# capitalize() --- заглавная буква
# f_s_n=[]
# s_s_n=[]
# a=input('names: ').split()

# for name in a:
#     if len(name)>4:
#         f_s_n.append(name)
# print(f_s_n)


# for i in range(10):
#     print(i)

# ******************************


# while  3>2:
#     print(f"  i work")
    

# i=0
# num=3
# while num>i:
#     print('i work')
#     i +=1





# types =(str, int, float, list, tuple)
# for value in types:
#     print(value, True if '__iter__' in dir(value) else False)


# lists=['Ermek', 'Aidana', 'Tima', 'Bermet', 'Zhanylai']
# sred =len(lists)//2
# for name in lists:
#     if name.lower()=='aidana':
#         continue
#     print(f'hi {name}!')

# lists.insert(sred, 'Ramazan')
# for name in lists:
#     if name=='Ramazan':
#         break
#     print(f'hi {name}!')
# a=bool(1)
# while a:
#     if input('enter ur name:') in 'war drags black'.split():
#         print('your blacked')
#         break


#1)input(Email) 2)show Emails 
# crud create delete read update

# DB_EMAILS=[]
# while True:
#     print('1)) Input Email 2) Show db_emails 3) Delete email in DB 4)stop while 5)rename email')
#     choices = int(input('enter choice'))
#     if choices==1:
#         email=input('enter email:')
#         if email.endswith('@gmail.com'):
#             if email in DB_EMAILS:
#                 print('email exists')
#                 continue
#             DB_EMAILS.append(email)
#             continue
#         print('Invalid email, only GMAIL')
        

#     elif choices==2:
#         print(DB_EMAILS)
#     elif choices==3:
#         email=input('enter email:')
#         if email in DB_EMAILS:
#             # index=DB_EMAILS.index(emai)
#             # DB_EMAILS.pop(index)
#             DB_EMAILS.remove(email)
#         else:
#             print(f'{email} doesnt exist')
#     elif choices==4:
#         break
#     elif choices==5:
#         old_email=input('enter old email:')
#         if email in DB_EMAILS:
#             new_email=input('enter new email:')
#             if email.endswith('@gmail.com'):
#                 DB_EMAILS.remove(old_email)
#                 DB_EMAILS.append(new_email)
               
#     else:
#         print('Error')
    
 




