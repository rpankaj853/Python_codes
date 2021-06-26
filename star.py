"""n= 65
for i in range(0,5):
    for j in range(0,i+1):
        ch = chr(n)
        print(ch ,end=" ")
    n = n+1
    print()"""
x =int(input())
y = int(input())
print(x,y)
x,y = y,x
print(x,y)
