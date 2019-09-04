n = int(input())
if n >= 1 and n <= 4:
    print('несколько')
elif n >= 5  and n <= 9:
    print('	немного')
elif n >= 10 and n <= 19:
    print('	отряд')
elif n >= 20 and n <= 49:
    print('	толпа')
elif n >= 50 and n <= 99:
    print('	орда')
elif n >= 100 and n <= 249:
    print('множество')
elif n >= 250 and n <= 499:
    print('сонмище')
elif n >= 500 and n <=999:
    print('полчище')
elif n >= 1000:
    print('	легион')