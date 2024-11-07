'''googled https://www.geeksforgeeks.org/how-to-take-multiple-inputs-using-loop-in-python/ to find how to keep the user inputs stored'''
'''googled https://www.swhosting.com/en/comunidad/manual/the-5-ways-to-find-the-average-of-a-list-in-python#:~:text=to%20find%20it.-,Way%201%3A%20Using%20the%20sum()%20and%20len()%20function,of%20a%20list%20in%20Python. to find how to maths'''








inputs = []
number = int(input("Please enter a number : "))

while number > -1 or number < -1 :
    inputs.append(number)
    number = int(input("Please enter a number : "))
    continue 
num_average = sum(inputs) / len(inputs)
print(f"{num_average}")