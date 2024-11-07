









user_input = input("Please enter your name : ")
user_input_list = []
while "jhon" not in user_input_list :
    user_input_list.append(user_input)
    user_input = input("Please enter your name : ")
else : 
    print(f"incorrect names : {user_input_list}")