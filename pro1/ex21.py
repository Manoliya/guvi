p7=int(input())
r7=list(map(int,input().split()))
a7=int(p7/2)
laa=r7[:a7]
lb=r7[a7::]
if ((sum(laa)//len(laa))==(sum(lb)//len(lb))):
    print("yes")
else:
    print("no")
