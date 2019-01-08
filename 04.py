N = 5
for i in range(0,N+1):
    
    for j in range(i,N):
        print(" ",end='')
        
    for k in range(0,i):
        print("*",end='')
        
    for l in range(1,i):
        print("*",end='')

    print()
