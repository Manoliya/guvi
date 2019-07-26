n7,m7=map(int,input().split())
tem=[]
x7=0
for m in range(n7):
    tem.append(list(map(int,input().split())))   
for m7 in range(n7):
    for j in range(m7-1):
        for k in range(j+1,m7+1):
            if tem[m7][j:k]==[1]*len(tem[m7][j:k]):
                 if all(tem[p+m7][j:k]==[1]*len(tem[p+m7][j:k]) for p in range(len(tem[m7][j:k])-1)):
                     if len(tem[m7][j:k])>x7:
                        x7=len(tem[m7][j:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
    print(1)
for m7 in range(x7):
    print(*[1]*x7) 
