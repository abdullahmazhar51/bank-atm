#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to YES bank ATM")
restart = ('Y')
chances = 3
balance = 30000
while chances >= 0:
    pin = int(input("Please Enter you 4 digit pin"))
    if pin == (1234):
        print("you have entered the pin correctly\n")
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 to make a Withdraw\n')
            print('Please Press 3 to Pay in\n')
            print('Please Press 4 to Return card\n')
            option = int(input('What would you like to choose?'))
            if option == 1:
                print('your balance is 300000')
                restart = input('would you like to go back?\n')
                if restart in ('n', 'NO', 'no', 'N'):
                    print("thankyou")
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('how much would you like to withdraw?\n'))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print('remaining balancee is', balance)
                    restart = input('would you like to go back?')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('thankyou')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid amount, please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input("Please enter correct amount:"))
        
            elif option == 3:
                Pay_in = float(input('How much would you like to pay in?'))
                balance = balance + Pay_in
                print('\nYour balance is', balance)
                restart = input('would you like to go back?')
                if restart in ('n', 'No', 'no', 'N'):
                    print('thankyou')
                    break
            elif option== 4:
                print('Please wait whilst your card is returned...\n')
                print('thankyou for your service')
                break
            else:
                print('Please enter the correct pin\n')
                restart = ('y')
    elif pin != ('1234'):
            print('Incorrect Pin')
            chances = chances - 1
            if chances == 0:
                print('\n No more tries')
                break
        


# In[ ]:




