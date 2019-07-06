z_list = [2,32,1,2,5,3,7,8,2,2,1,0,9]
j = 0
for i in range(1,14):
    if z_list[i] > z_list[j]:
        print(z_list[i])
    j += 1

