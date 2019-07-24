a7=int(input())
n7=list(map(int,input().split()))
l7=[]
for i in n7:
  k=bin(i)
  l7.append(k)
f=sorted(l7)
f.reverse()
for j in f:
  print(int(j,2))
