
lists = []
y =  []
for i in range(0,5):
    ele = int(input())
    lists.append(ele)
for i in range(0,len(lists)):
    print(lists[i],lists.count(lists[i]))
    
for i in range(0,len(lists)):
    if lists.count(lists[i]) >= 2:
        
        x = str(lists[i])
        y.append(x)
        
print(y)

y = list(set(list(map(int,y))))
print(" ".join(map(str,y)))
    


   
