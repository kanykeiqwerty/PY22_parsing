# with open('tr.txt','r') as a:
#     for line in a.readlines():
#         print(max(line))

with open('input.txt', 'r') as f:
    a = []
    for i in f.read().split():
        a.append(int(i))
with open('output.txt', 'w') as fs:
    fs.write(str(max(a)))
    fs.write(str(min(a)))
    # print(max(a), file=fs)
    # print(min(a), file=fs)   