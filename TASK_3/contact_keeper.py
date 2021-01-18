from ContactRecord import ContactRecord

def displayContactBook(plist):
    print("Name                          Contact Number(s)")
    print("____                          _________________\n")
    nSpaces = 30
    sp = " "
    for person in plist:
        print(person.name + sp*(nSpaces - len(person.name)), end = "")
        if person.contactNumber:
            for contact in person.contactNumber:
                print(contact, end = " ")
            print("\n", end = "")
        else:
            print("------")

def userMenu():
    personList = []
    morePersons = True
    numberOfPersons = 1
    while True:
        print("""\nPlease use the following menu to perform various operations on the contact book.
                1. Add a new contact detail
                2. Display the current contents of the contact book
                3. Search the contact book using a keyword
                4. Exit from the menu\n""")
        choice = input("Press the number corresponding to the operation of your choice from the above menu: ")
        if choice == '1':
            personContact = ContactRecord()
            personContact.inputPersonDetails()
            if personList:
                i = 0
                l = len(personList)
                while i < l and personContact.name.lower() >= personList[i].name.lower():
                    i += 1
                
                personList.insert(i, personContact)
    
            else:
                personList.append(personContact)

        elif choice == '2':
            if personList:
                displayContactBook(personList)
            else:
                print("Oops!! please first add some contact details\n")

        elif choice == '3':
            key = input("\nPlease enter the keyword for searching the contact book with: ").lower()
            matches = 0
            matchedPersonList = []
            if personList:
                for person in personList:
                    lcaseName = person.name.lower()
                    if lcaseName.find(key) > -1:
                        matches += 1
                        matchedPersonList.append(person)
                
                print("\nThere is/are " + str(matches) + " match(es)\n")
                if matches > 0:
                    print("The matched list of names are:\n")
                    i = 0
                    for person in matchedPersonList:
                        i += 1
                        print(str(i) + ". " + person.name)

                    print("\nNow you can select only one among the above displayed person names to see their contact details\n")
                    index = int(input("For selection, Please type the serial number corresponding to the person name whose contact details you want to be displayed: "))
                    while index not in range(1, len(matchedPersonList) + 1):
                        print("Invalid Serial Number!!\n")
                        index = int(input("For selection, Please type the serial number corresponding to the person name whose contact details you want to be displayed: "))
                    
                    
                    
                    print("\nThe selected person's details are")
                    print("------------------------------------")
                    print("Name: " + matchedPersonList[index - 1].name)

                    if person.contactNumber:
                        print("Contact Number(s): ", end = "")
                        for contact in person.contactNumber:
                            print(contact, end = " ")
                        print("\n")
                    else:
                        print("------")
            else:
                print("Sorry!! The contact book is empty\n")
        else:
            exit(0)

def main():
    userMenu()

if __name__ == "__main__":
    main()
