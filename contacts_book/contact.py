#To build a simple contact book using dictionary 
def contact_book():

    contacts = {}
    print("")
    print('='*37)
    print("   Welcome to Contact book.    ")
    print('='*37)
    while True:

        print('*'*37)
        print("Choose numbers:-")
        print(" 1. Add contact\n 2. Search contact\n 3. Delete contact\n 4. Display all contacts\n 5. Exit")
        print('*'*37)
        try:
            n=int(input("-> "))
        except ValueError:
            print("Please enter a number only.")
            continue

        if 5>=n>=1:
            #Add contact
            if n==1:
                name = input("Enter name: ")
                number = input("Enter contact number: ")
                if name in contacts:
                    print("\n--| This name already exists! |--\n")
                else:
                    contacts[name] = number
                    print("\n--| Contact added successfully. --|\n")

            #Search contact
            elif n==2:
                name_search = input("Enter name: ")
                if name_search in contacts:
                    print("")
                    print(37*'-')
                    print("(Contact found.)")
                    print(f"Name\t: {name_search}\nNumber\t: {contacts.get(name_search)}")
                    print(37*'-',"\n")
                else:
                    print("\n--| Contact not found. --|\n")

            #Delete contact
            elif n==3:
                name_del = input("Enter name: ")
                if name_del in contacts:
                    del contacts[name_del]
                    print('\n--|',"Deleted successfully. |--\n")
                else:
                    print("\nContact not found.\n(Maybe you entered incorrect name)\n")

            #Display all contacts
            elif n==4:
                if not contacts:
                    print("\n--| Contact book is empty! |--")
                else:
                    for i in contacts:
                        print(37*'-')
                        print(f"Name\t: {i}\nNumber\t: {contacts[i]}")
                        print(37*'-',"\n")

            #Exit
            elif n==5:
                print("All saved contacts will be deleted!")
                while True:
                    n_exit = input("Are you sure? (yes/no): ")
                    if n_exit == "yes":
                        print("\n--|Thanks for using contact book.|--\n")
                        return
                    elif n_exit == "no":
                        print("")
                        break
                    else:
                        print("\nPlease enter words correctly.")
                        continue
        else:
            print("Please choose correct number!")

contact_book()
