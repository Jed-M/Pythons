import math









product1 = input("Please enter the name of a product : ")
product2 = input("Please enter the name of another product : ")
product3 = input("Please enter the name of one last product : ")
price1 = input("Please enter the price of the first product to two decimal places : ")
price2 = input("Please enter the price of the second product to two decimal places : ")
price3 = input("Please enter the price of the third product to two decimal places : ")
price1_fl = float(price1)
price2_fl = float(price2)
price3_fl = float(price3)
total = price1_fl + price2_fl + price3_fl
price1_round = round(price1_fl)
price2_round = round(price2_fl)
price3_round = round(price3_fl)
total_round = price1_round + price2_round + price3_round
print(f"The total of {product1}, {product2} and {product3} is R{total} and the average price of the items is R{total_round}.")