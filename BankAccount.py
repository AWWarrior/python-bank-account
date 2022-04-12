money_in_bank=1000000
print("You currently have $1000000 in the bank.")
while money_in_bank!=0:
    money_withdrawn=input("How much money do you want today?")
    money_withdrawn=int(money_withdrawn)
    money_in_bank=money_in_bank-money_withdrawn
    if money_in_bank >0:
        print("You have $%s left in your bank" % money_in_bank)
    else:
        print("Sorry! Your're out of cash!")
        break
