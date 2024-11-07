import math









'''investment = "investment"
bond = "bond" '''


print("Investment - to calculate the amount of intrest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")
print()
user_choice = input("Enter either 'Investment' or 'Bond' from the menu above to proceed : ")


if user_choice in ['investment' , 'Investment' , 'INVESTMENT']: 
    inves_deposit = float(input("How much money are you depositing : "))
    inves_intrest = float(input("Please enter the percentage intrest rate : "))
    inves_intrest_decimal = inves_intrest / 100 
    inves_duration = float(input("How many years do you plan on investing : "))
    simple_intrest_total = inves_deposit *(1 +inves_intrest_decimal*inves_duration)
    compound_intrest_total = inves_deposit * math.pow((1+inves_intrest_decimal),inves_duration)
    intrest = input("Would you like simple or compound intrest : ")
    if intrest in ['simple' , 'Simple' , 'SIMPLE']:
        print(f"{simple_intrest_total}")
    elif intrest in ['compound' , 'Compound' , 'COMPOUND']:
        print(f"{compound_intrest_total}")
    else :
        print("Please make sure to spell the words correctly")
elif user_choice in ['bond' , 'Bond' , 'BOND']:        
    current_house_value = float(input("Please enter the current value of the house : "))
    annual_intrest_rate = float(input("Please enter the percentage intrest rate : "))
    bond_repay_months = float(input("How many months do you plan to repay the bond (e.g. 24 ) : "))
    annual_intrest_rate_decimal = annual_intrest_rate / 100
    monthly_intrest_rate = annual_intrest_rate_decimal / 12
    monthly_user_payment = (monthly_intrest_rate * current_house_value)/(1-(1 + monthly_intrest_rate)**(-bond_repay_months))
    print(f"{monthly_user_payment}")
else :
    print("Please make sure to spell the words correctly")






