
#get details of loan
money_owed = float(input('How much money do you owe in dollars?\n')) 
apr = float(input('What is the annual percentage rate of your loan?\n'))
payment = float(input('How much will you pay per month?\n'))
months = int(input('How many months do you want to see the results for?\n'))

monthly_rate = apr/100/12 #divde by 100 to convert to precentage and by 12 to convert from years to monthly interest rate. 

for i in range(months):
    #calculate interest to be paid:
    interest_paid = money_owed*monthly_rate

    #Add interest
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the in', i+1, "months")
        break
    #make payment
    money_owed = money_owed - payment

    #give results
    print('Paid', payment, 'of which', interest_paid, 'was interest', end=' ')
    print('Now you owe', money_owed)