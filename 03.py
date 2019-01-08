N = 5

for i in range(0,N):
    for k in range(i,N-1):
        print(" ",end='')
    for j in range(0,i+1):
        print("x",end='')
    print()
