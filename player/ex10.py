s7,s8=input().split()
C7=0
for i in range(0,len(s7)):
    for j in range(0,i+1):
        if s7[i]!=s8[j]:
            C7+=1
            break
if C7==1:
    print("yes")
else:
    print("no")
