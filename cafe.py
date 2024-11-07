









menu = ["coffee" , "cake" , "cheetos" , "whole cow"]
stock = {'coffee' : '100' , 'cake' : '50' , 'cheetos' : '400' , 'whole cow' : '2000000'}
price = {'coffee' : '10' , 'cake' : '20' , 'cheetos' : '5' , 'whole cow' : '1000'}
total_stock = float(stock['coffee']) * float(price['coffee']) + float(stock['cake']) * float(price['cake']) + float(stock['cheetos']) * float(price['cheetos']) + float(stock['whole cow']) * float(price['whole cow'])
print(f"Total stock value is equal to R{total_stock}.")





'''menu = ["coffee" , "cake" , "cheetos" , "whole cow"]
stock = {'coffee' : '100' , 'cake' : '50' , 'cheetos' : '400' , 'whole cow' : '2000000'}
price = {'coffee' : '10' , 'cake' : '20' , 'cheetos' : '5' , 'whole cow' : '1000'}
for i in menu:
    total_stick_value = int(stock[0:3]) * int(price[0:3])
    print(total_stick_value)'''
    