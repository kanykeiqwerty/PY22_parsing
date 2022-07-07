DB_EMAILS=[]
while True:
    print('1)) Input Email 2) Show db_emails 3) Delete email in DB 4)stop while 5)rename email')
    choices = int(input('enter choice'))
    if choices==1:
        email=input('enter email:')
        if email.endswith('@gmail.com'):
            if email in DB_EMAILS:
                print('email exists')
                continue
            DB_EMAILS.append(email)
            continue
        print('Invalid email, only GMAIL')
        

    elif choices==2:
        print(DB_EMAILS)
    elif choices==3:
        email=input('enter email:')
        if email in DB_EMAILS:
            # index=DB_EMAILS.index(emai)
            # DB_EMAILS.pop(index)
            DB_EMAILS.remove(email)
        else:
            print(f'{email} doesnt exist')
    elif choices==4:
        break
    elif choices==5:
        old_email=input('enter email:')
        if email in DB_EMAILS:
            new_email=input('enter new email:')
            if email.endswith('@gmail.com'):
                DB_EMAILS.remove(old_email)
                DB_EMAILS.append(new_email)
               
    else:
        print('Error')
    
 
# 1)отменя выбора
# 2)оптимизация
# 3)




