









full_name = input("Please enter your full name : ")
if len(full_name) == 0 :
    print("You havent enterd anything.Please enter your full name.")

elif len(full_name) <= 4 :
        print("You have enterd less than 4 characters. Please make sure that you have enterd your name and surname.")

elif len(full_name) >= 25 :
        print("You have enterd more than 25 characters. Please make sure that you have only enterd your full name.")

else :
    print("Thank you! ^-^")