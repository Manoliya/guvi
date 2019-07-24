a7=int(input())
b7=[int(i) for i in input().split()]
xxx=0
for i in range(a7):
   for j in range(i):
      if b7[j]<b7[i]:
         xxx+=b7[j]
print(xxx)
