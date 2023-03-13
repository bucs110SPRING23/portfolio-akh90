
amount = input("enter the amount: ")
amount  = float(amount) #this is the same thing as wrapping float around amount (could b done in previous line)
rate = input("enter the exchange rate: ")
rate = float (rate)
new_amount = amount * rate
minus_fees = new_amount - 3
print ("your result minus a lil tip (4 me!) is: ", minus_fees)




