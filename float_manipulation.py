import math


'''sauce https://stackoverflow.com/questions/21043387/how-do-you-add-input-from-user-into-list-in-python'''






'''number_list = []

float1 = input("Please enter a number and decimal:")
number_list.append(float1)
float2 = input("Please enter another number and decimal:")
number_list.append(float2)
float3 = input("Please enter another number and decimal:")
number_list.append(float3)
float4 = input("Please enter another number and decimal:")
number_list.append(float4)
float5 = input("Please enter another number and decimal:")
number_list.append(float5)
float6 = input("Please enter another number and decimal:")
number_list.append(float6)
float7 = input("Please enter another number and decimal:")
number_list.append(float7)
float8 = input("Please enter another number and decimal:")
number_list.append(float8)
float9 = input("Please enter another number and decimal:")
number_list.append(float9)
float10 = input("Please enter another number and decimal:")
number_list.append(float10)


print(sum(int(number_list)))'''

number_list = []
number_list_length = 10

while len(number_list) < number_list_length:
    number = input("PLease enter a number and decimal :")
    number_list.append(number)
print(number_list)



