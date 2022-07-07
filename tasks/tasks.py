# import random
# import string



# letter1 = random.choice(string.ascii_uppercase)
# # print(string..ascii_uppercase)

# letter2 = random.choice(string.ascii_uppercase)
# number = random.randint(1, 10)
# simbols = random .choice(string.punctuation)
# # print(letter1, letter2, number, simbols)
# password =[letter1, letter2, str(number), simbols]
# random.shuffle(password)
# password = '.'.join(password)
# print(password)




def getway(a, b):
    d=0
    s=0
    for x in b:
        if x=='u':
            s+=1
            if s==0:
                d+=1
        elif x=='d':
            s-=1
    return d
print(getway(12, 'dduudduduuud'))

    
            
            


