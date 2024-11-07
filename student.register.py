









student_amount = input("How many students are registering for the exam : ")
student_length = len(student_amount)
with open('output.txt', 'w') as f:
    f.write(student_amount+"\n")
for i in student_amount:
    print("Please enter student ID : ")