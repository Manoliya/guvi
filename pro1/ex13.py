m7,n7=map(int,input().split())
k7=[]
s7=[]
a7=[int(m7) for m7 in input().split() ]
for i in range(0,n7):
    u7,v7=map(int,input().split())
    for j in range(u7-1 ,v7):
        s7.append(a7[j])
    x7=sorted(s7)
    k7.append(min(s7))
    del s7[:]
for z in range(0,len(k7)):
    print(k7[z])
