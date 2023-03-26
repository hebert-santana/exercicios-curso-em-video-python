a = list()

a.append('Galo')
a.append(13)

print(a)

b = list()
b.append(a[:])
print(b)

a[0] = 'Doido'
a[1] = 777

b.append(a[:])
print(b)