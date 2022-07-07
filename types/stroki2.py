# #  # # strok way
# # # # # dir() function taking ways of types of dannyh
# # # # # print(dir(str))
# # # # '<soedenitel'.join(<massiv kotoryi nujno soedenit>) - soedinyaet massiv iz strok po soedenitelu v 1 tochku
# ls=['milk', 'bread', 'water', 'apple', str(5)]
# joined = '!'.join(ls)
# print(joined)
# # split(rasdelitel) -> drobit stroku po rasdelitelu i vosvrashyaet tip dannyh list.
# text = 'milk, bread, water, apple'
# splited = text.split('. ')
# print(splited)
# joined = '. '.join(splited)
# print(joined)
#replace(cod value, new value, [count])
# -> menyaet v stroke znacheniye old na new value, esli vy ukajite count, to on zamenit count ras

# text = "ha ha ha ha ha"
# replaced = text[:3] + text[3:].replace('ha', 'john' )
# print(replaced)


# strip()-> ubiraet probelnye simbolt v nachale i v konce stroki

# rstrip() remove in the end
# lstrip()remove in the begin


# text = input('enter full name  ')
# print(text.strip())
# print(text.lstrip)
# print(text)


#count('simbol') counting kolichestvo <simbol> v stroku

# text = 'hello world! i\'m from Earth'
# print(text.count('l'))

#index('', [start], [end]) -> vyvodit index znachenie value v nashei stroke

# text='hello world! thi is makers'
# result = text.index('i')
# print(result)
# print(len(text))
# print(text.find('w'))
