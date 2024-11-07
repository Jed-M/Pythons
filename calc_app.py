with open('equations.txt' , 'a+') as file:
    text = "I lied there are no previous equations here..."
    file.write(text)
    number_1 = float(input("Please input a number for calculation :"))
    symbol = input("Please select a function (multiply *), (divide /), (addition +), (subtraction -) :")
    number_2 = float(input("Please input a second number for calculation :"))
    user = input("If u would like to see all previous equations please type 'yes' else type 'no' :")
    lines = file.readlines
    

    try : 

        if symbol == "+":
            math = number_1 + number_2
            print(math)
        elif symbol == "-":
            math = number_1 - number_2
            print(math)
        elif symbol == "*":
            math = number_1 * number_2
            print(math)
        elif symbol == "/":
            math = number_1 / number_2
            print(math)
        else :
            print("Please enter a symbol from the list of symbols")

    except Exception:
        print("You broke it, try again...    ...but dont do that again :")
    finally:
        if user == "yes":
            print(lines)
        else :
            file.close()