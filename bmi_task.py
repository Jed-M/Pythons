









weight = float(input("Please enter your weight in Kilograms: "))
height = float(input("Please enter your height in Meters : "))
bmi = weight / height ** 2 
if bmi >= 30 :
    print(f" {bmi} You are obese")
elif bmi >= 25 < 30 :
     print(f" {bmi} You are overweight")
elif bmi >= 18.5 < 25 :
      print(f" {bmi} You are normal")
else :
      print(f" {bmi} You are underweight")