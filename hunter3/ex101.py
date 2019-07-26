N7=int(input())
a7=[]
c7=0
for i in range(2,N7):
    for j in range(2,i+1):
        if i%j==0:
            break
    if j==i:
        a7.append(i)
for i in range(len(a7)):
    for j in range(len(a7)):
        for k in range(len(a7)):
            if a7[i]+a7[j]+a7[k]==N7:
                print(str(a7[i])+" "+str(a7[j])+" "+str(a7[k]))
                c7=1
                break
        if c7==1:
            break
    if c7==1:
        break
