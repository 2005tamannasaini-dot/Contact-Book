##  CONTACT BOOK PROJECT
 
contacts = []

print("===== CONTACT BOOK =====")
print("1. ADD CONTACT")
print("2. VIEW CONTACT")
print("3. SEARCH CONTACT")
print("4. DELETE CONTACT")
print("5. EXIT")

while True:
    choice = int(input("Enter Your Choice:"))

    if choice == 1 :
        name = input("Enter your Name:")
        phone = int(input("Enter Your Phone No.:"))

        contact = {"name" : name,
                   "phone": phone}

        contacts.append(contact)

        print("Contact added successfully!")

    elif choice == 2 :
        if len(contacts) == 0:
            print("NO Contact Available.")

        else:
            print("==== CONTACTS ====")

            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])