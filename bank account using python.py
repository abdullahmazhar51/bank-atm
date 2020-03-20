#!/usr/bin/env python
# coding: utf-8

# In[10]:


class bankaccount:
    def __init__(self, balance):
        self.balance = 0
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        
        if self.balance >= amount:
            self.balance -= amount
        else: 
            print("insufficient balance")
    
    def print_balance(self):
        return self.balance


# In[18]:


a1 = bankaccount(0)
a1.deposit(100)
print(a1.balance)
a1.withdraw(500)
a1.deposit(5000)
a1.withdraw(3499)
print(a1.balance)


# In[ ]:




