class ContactRecord:
    def __init__(self):
        self.name = ""
        self.contactNumber = []

    def inputPersonDetails(self):
        moreContacts = True
        numberOfContacts = 1
        self.name = input("\nEnter the name of the person: ")
        while moreContacts:
            self.contactNumber.append(input("Enter the person's contact number " + str(numberOfContacts) + ": "))
            multipleContacts = input("Do you want to enter more contact numbers (Press 'y' for yes and 'n' for no): ")
            if multipleContacts == 'n':
                moreContacts = False
            else:
                numberOfContacts += 1
