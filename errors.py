# This example program is meant to demonstrate errors.


print("Welcome to the error program")
print("\n")                                      #no brackets # random indent

    
age_str = "24"      #too many = symbols 
age = int(age_str) 
print(f"I'm {age} years old.")

    
years_from_now = 3
total_years = age + years_from_now

print(f"{total_years} , {years_from_now}")

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6
print(f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer
