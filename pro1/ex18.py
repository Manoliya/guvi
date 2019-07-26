n7,m7=map(int,input().split())
te=[]
x7=0
for m in range(n7):
    te.append(list(map(int,input().split())))   
for m7 in range(n7):
    for j in range(m7-1):
        for k in range(j+1,m7+1):
            if te[m7][j:k]==[1]*len(te[m7][j:k]):
                 if all(te[p+m7][j:k]==[1]*len(te[p+m7][j:k]) for p in range(len(te[m7][j:k])-1)):
                     if len(te[m7][j:k])>x7:
                        x7=len(te[m7][j:k])
if len(te)==1 and len(te[0])==1 and te[0][0]==1:
    print(1)
for m7 in range(x7):
    print(*[1]*x7) 
