ax7,ay7=map(int,input().split())
m7=list(map(int,input().split()))
m7.sort()
m7.reverse()
ah7=ay7
Z7=0
for i in m7:
    if(ah7>=i):
        no=int(ah7/i)
        Z7=Z7+no
        ah7=ah7-no*i
    if ah7==0:
        break
if(ah7==0):
   print(Z7)
else:
   print("it is not posible to select coins ",S)  
