N = 9

x=int(N/2)
y=N-x

for i in range(0,x+1):
    for j in range(0,i):
        print("*",end='')
    print()
    
for k in range(y,0,-1):
    for j in range(0,k):
        print("*",end='')
    print()
        
