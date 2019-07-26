X7=int(input())
t7=[]
for i in range(0,X7):
    l=list(map(int,input().split()))
    for j in l:
        t7.append(j)
print(*sorted(t7),end="")
