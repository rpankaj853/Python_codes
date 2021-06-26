val = int(input());
ans = 0;
while(val > 0):
    rem = val %10;
    ans = ans*10 + rem;
    val = val // 10;

print(ans);    
    
    
    
