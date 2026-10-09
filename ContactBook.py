##  CONTACT BOOK PROJECT
 
contacts = []

while True:

    print("===== CONTACT BOOK =====")
    print("1. ADD CONTACT")
    print("2. VIEW CONTACT")
    print("3. SEARCH CONTACT")
    print("4. DELETE CONTACT")
    print("5. Update Contact.")
    print("6. EXIT")


    choice = int(input("Enter Your Choice:"))

    if choice == 1 :
        while True:

            name = input("Enter your Name:")
            
            if name.strip():
                break

            print("Name cannot be empty.")

        while True:
            phone = input("Enter Your Phone No.:")

            if phone.isdigit() and len(phone) == 10:
                break

            print("Please enter a valid 10-digit phone number.")
            
        duplicate = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                duplicate = True
                break

        if duplicate:
            print("Contact already exists!")
        else:
            contact = {"name" : name,
                    "phone": phone}

            contacts.append(contact)

            print("Contact added successfully!")

    elif choice == 2 :
        if len(contacts) == 0:
            print("NO Contact Available.")

        else:
            print("==== CONTACTS ====")

            sorted_contact = sorted(contacts, key=lambda contact : contact["name"].lower())

            for contact in sorted_contact:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])

    elif choice == 3 :
        search_name = input("Enter contact Name to search: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                found = True

        if not found :
            print("Contact not found.")        

    elif choice == 4 :
        delete_name =  input("Enter contact Name to Delete : ")        

        found = False

        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact Delete Successfully!.")
                found = True
                break

        if not found: 
            print("Contact not found.")   

    elif choice == 5 :  
        update_name = input ("Enter contact Name to Update: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == update_name.lower():

                while True:
                    new_phone =input("Enter new phone number:")

                    if new_phone.isdigit() and len (new_phone) ==10:
                        break

                contact["phone"] = new_phone

                print("Contact updated successfully!")
                found =True
                break

        if not found:
            print("Contact not found.")


    elif choice == 6 :
        print("Thank Your for using Contact Book.")
        break

    else:
        print("Invalid Choice! Please Select 1 to 5. ")