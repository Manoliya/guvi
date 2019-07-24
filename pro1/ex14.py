vj7,vk7=map(int,input().split())
l7=list(map(int,input().split()))
vj7=[]
l7.insert(0,0)
for a in range(vk7):
     v7=[]
     sumup=0
     cc,dd=map(int,input().split())
     for b in range(cc,dd+1):         
         sumup^=l7[b]     
     vj7.append(sumup)
for c in vj7:
    print(c)
