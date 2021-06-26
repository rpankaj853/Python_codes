def fabi():
    a = int(input("enter first value"))
    b = int(input("enter second value"))
    while(b < 10):
        print(b)
        a,b = b,a+b
         
fabi();
