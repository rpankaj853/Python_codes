n = int(input())
fact = 1

for i in range(1,n+1):
    fact = fact * i

count= 0 
while(fact>0):
    a = fact % 10
    if a == 0:
        count += 1
    elif a != 0 :
        break 
    fact = fact //10
        
    
print(count)
