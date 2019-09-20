import random
'''
for line in f:
    print(line)

lt = f.read().split()
print(lt)
print(lt[1:])
'''
lista = ['A', 'B', 'C', 'D']
key = []
val = []
for i in range(len(lista)):
    key.append(lista[i])
    val.append(lista[i+1:])
    #print(lista[i], lista[i+1:])
# print(key)
# print(val)
dic = dict(zip(key, val))
print(dic)

a = []
for i in dic.keys():
    lis = dic[i]
    if not lis:
        break
    a.append(random.choice(lis))

print(dic['A'][0], a[2])
