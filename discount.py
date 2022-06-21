def amount():
    units = int(input("Enter quantity: "))
    total_cost = units * 100
    bonus = total_cost * 0.1
    discount = total_cost - bonus
    if total_cost > 1000:
        print(f"From your total cost {total_cost}, you have a received a bonus of {bonus} and you will only pay {discount}")
    else:    
         print(f"Your total cost is {total_cost}")
amount()    