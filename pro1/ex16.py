a7=int(input())
c7=list(map(int,input().split()))
x7=[1]*a7
for p in range(a7):
    if p==0:
        if c7[p]>c7[p+1]:
            x7[p]=x7[p]+x7[p+1]
    elif p>0:
        if c7[p]>c7[p-1]:
            x7[p]=x7[p]+x7[p-1]
print(sum(x7))
