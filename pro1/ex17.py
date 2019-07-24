x7,j7=map(int,input().split())
y7=list(map(int,input().split()))[:x7]
count7=0
for k in range(0,len(y7)-1):
  for sec in range(k+1,len(y7)-1):
    if(y7[k]+y7[sec]==j7):
      count7+=1  
if count7==1:
  print("yes")
else:
  print("no")
