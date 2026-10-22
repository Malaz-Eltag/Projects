# Code Frome The Internet 
# accounts_numbers=[23410324,132432,9865665,596900,4654680,76432,86785342,5678888,734533,456045456]
# accounts_passkeys=[2344,5433,7523,9806,4560,6454,5343,6565,3455,5677]
# accounts_balances=[0,0,0,0,0,0,0,0,0,0]

# account_num=int(input('welcome, to atm, enter your account number:'))
# found_account=False
# counter=-1
# for a in accounts_numbers:
#     counter=counter+1
#     if a==account_num:
#         found_account=True
#         break;

# if found_account == False:
#     print('account number does not exists')
# else:
#     passkey=int(input('enter your passkey'))
#     if passkey==accounts_passkeys[counter]:
#         choice=int(input('1.withdraw money.\n2.transfer money to another account.\n3.deposit money.\n4.display balance.\n'))
#         if choice==1:
#             money=int(input('enter money amount:'))
#             if money>accounts_balances[counter]:
#                 print('not enough money in your balance')
#             else:
#                 accounts_balances[counter]=accounts_balances[counter]-money
#         elif choice==2:
#             money = int(input('enter money amount:'))
#             if money > accounts_balances[counter]:
#                 print('not enough money in your balance')
#             else:
#                 c=int(input('enter account number you want to transfer to:'))
#                 count=-1
#                 for a in accounts_numbers:
#                     count=count+1
#                     if a==c:
#                         accounts_balances[counter] = accounts_balances[counter] - money
#                         accounts_balances[count]=accounts_balances[count]+money
#                         break
#         elif choice==3:
#             money=int(input('inter money amount:'))
#             accounts_balances[counter] = accounts_balances[counter] + money
#         elif choice==4:
#             print('your balance equal',accounts_balances[counter])



# Code after Modification

accounts_numbers=[23410324,1324321,9865665,596900,4654680,76432,86785342,5678888,734533,456045456]
accounts_passkeys=[2344,5433,7523,9806,4560,6454,5343,6565,3455,5677]
accounts_balances=[0,3400,431200,455490,566590,344453,32422,2434696,645533,879760]
    
while True:
   
    account_num=int(input('welcome, to ATM, enter your account number:'))
    found_account=False
    counter=-1
    for a in accounts_numbers:
        counter=counter+1
        if a==account_num:
            found_account=True
            break
    
    if found_account == False:
            print('account number does not exists, please try again ')
    else:
        passkey=int(input('enter your passkey :'))
        if passkey==accounts_passkeys[counter]:
            choice=int(input('1.withdraw money.\n2.transfer money to another account.\n3.deposit money.\n4.display balance.\n'))
        else :
            print("wrong Passkey")
            ans=input("Do you Wante :\n1.Try Again\n2.Exit\n")
            if ans=="1" :continue
            print("Thanks for choosing us")
            if ans== "2" : break
  
        if choice==1:
            money=int(input('enter money amount:'))
            if money>accounts_balances[counter]:
                print('not enough money in your balance, please try again')
                ans=input("Do You Wante Try Again With Another account ?\n1.Yes\n2.No\n")
                if ans=="1" :continue
                print("Thanks for choosing us")
                if ans== "2" : break          
                 
            if money <accounts_balances[counter]:
                accounts_balances[counter]=accounts_balances[counter]-money 
            if money < accounts_balances[counter]:
                        print("operation accomplished successfully \nDo you want make any operation ?\n1.Yes\n2.No") 
                        ans= input("")
                        if ans=="1" :continue
                        print("Thanks for choosing us")
                        if ans== "2" :break 
        if choice==2:
            money = int(input('enter money amount:'))
            if money > accounts_balances[counter]:
                    print('not enough money in your balance,please try again ')
                    ans=input("Do You Wante Try Again?\n1.Yes\n2.No\n")
                    if ans=="1" :continue
                    print("Thanks for choosing us")
                    if ans== "2" :break          
                        
                
            else:
                c=int(input('enter account number you want to transfer to:'))
                count=-1
                for a in accounts_numbers:
                    count=count+1
                if a==c: 
                    accounts_balances[counter] = accounts_balances[counter] - money
                    accounts_balances[count]=accounts_balances[count]+money                
                if money < accounts_balances[counter]:
                    print("operation accomplished successfully \nDo you want make any operation ?\n1.Yes\n2.No") 
                    ans= input("")
                    if ans=="1" :continue
                    print("Thanks for choosing us")
                    if ans== "2" :break         
                
        if choice==3:
                money=int(input('Enter money amount:'))
                accounts_balances[counter] = accounts_balances[counter] + money
                print("operation accomplished successfully \nDo you want make any operation ?\n1.Yes\n2.No")
                ans= input("")
                if ans=="1" :continue
                print("Thanks for choosing us")
                if ans== "2" :break      
                        
                else: 
                        print("")
        elif choice==4:
                        print('your balance equal',accounts_balances[counter])
                        print( "Do you want make any operation ?\n1.Yes\n2.NO") 
                        ans= input("")
                
                        if ans=="1" :continue
                        print("Thanks for choosing us")
                        if ans== "2" :break        
                    