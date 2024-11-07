









class Email():

    def __init__(self, email_adress, subject_line, email_content):

        self.email_adress = email_adress
        self.subject_line = subject_line
        self.email_content = email_content

    has_been_read = False

    def mark_as_read(self):
        
        has_been_read = True

    inbox_list = []

    def populate_inbox(self):

        email_one = ("example.email@email.co.za", "skoink", "this dosent work")
        email_two = ("example.email@email.co.za", "skoink", "this dosent work")
        email_three = ("example.email@email.co.za", "skoink", "this dosent work")


