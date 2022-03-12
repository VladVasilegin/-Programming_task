m,n = map(int,input().split())

leng = m*n


i = 0
j = 0
k = 1
k1 = 0
flag = True
while leng > 1 or not flag:
    if n-j >=2:
        print(f"{k} {k} ", end = '')
        k+=1
        j+=2
        leng -= 2
    elif n-j == 1:
        if m-i >= 2 and flag:
            print(f"{k}")
            leng -= 1
            k1 = k
            k += 1
            i += 1
            j = 0
            flag = False

        elif not flag:
            print(f"{k1}")
            leng -= 1
            i+=1
            j = 0
            flag = True
    else:
        i += 1
        j = 0
        print()
else:
    if leng == 1:
        print(f"{0}")



# if m%2 == 0:
#     k = m//2 * n
#     for i in range(m):
#         print(f"{k} " * n)
# elif n%2 == 0:
#     k = n//2 * m
#     for i in range(m):
#         print(f"{k} " * n)
# else:
#     k = m//2 * n + n//2
#     for i in range(m):
#         print(f"{k} " * n)

