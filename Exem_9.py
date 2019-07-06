Books = ['Как из топора кашу варили', 'Сказка о царе Салтане', 'А зори здесь тихие', 'Ночной дозор', 'Милые проказники']
a = 0
b = Books.append('Сумеречный дозор')
print(len(Books))
for i in range(0,len(Books)):
    a += len(Books[i])
print(a)


