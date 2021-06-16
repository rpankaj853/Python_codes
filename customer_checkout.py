#!/usr/bin/env python
# coding: utf-8

# In[5]:


def customer_timer(customer, cash_reg):
    if cash_reg == 1:
        d = sum(customer) 
        return d
    
    elif len(customer) <= cash_reg:
        a = max(customer)
        return a

    
# run according to len of cash_reg
    reg = {}
    for i in range(cash_reg):
   
       
        reg[i] = customer.pop(0)
        
    

    counts = 0
    while any(reg.values()):
        for i in reg.copy():
            
            #print(reg[i])
                   
            reg[i] -= 1
            
# catch negative values  
            if reg[i] <= 0:
                try:
                    reg[i] = customer.pop(0)
                except IndexError:
                    reg[i] = 0

        counts += 1
        
       

    return counts


# In[6]:


def mains():
    

    d = customer_timer([5, 1, 3], 1)
    
    print(d)
    
mains()


# In[ ]:



    


# In[ ]:





# In[ ]:




