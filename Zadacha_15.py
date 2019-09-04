a = int(input())
b = int(input())
for i in range(1, 100000):
    if a == i or b == i:
        print('yes')
    else:
        print('no')