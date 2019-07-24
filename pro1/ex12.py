a7,b7=map(int,input().split())
lis=list(map(int,input().split()))
l7=[]
for i in range(0,b7):
     u7,v7=map(int,input().split())
     l7.append([u7,v7])
for i in range(b7):
     lower=l7[i][0]
     upper=l7[i][1]
     s7=sum(lis[lower-1:upper])
     print(s7)
