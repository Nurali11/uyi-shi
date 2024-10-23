a = [0,4,8]
b = [0,4,6,8]
c = [i for i in b if i in a]
print(c)

if a == c:
    print('True')
else:
    print('False')
# print("".join(sorted("0,4,6,8")))