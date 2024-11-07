









class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office(self):
        print("Cape Town")



    


class OOPCourse(Course):
    def __init__(self, description, trainer):
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        print(f"This course is about "+self.description+" and the name of the overseeing trainer is "+self.trainer+".")

    def show_course_id(self):
        print("#12345")





course_1 = Course()
print(course_1)