# Kelly Pitts 09098321
contacts = {"Tommy":{"Nickname":"Tommy", "Name":"Tom Livingston", "Address": "32 Regents Road", "Phone Number":"09-958-2634"},
     "Alie":{"Nickname":"Alie","Name":"Alice Wonderland","Address":"55 Wonderway Park","Phone Number":"09-424-5962"}}

def display(name):
    print("Nick      Name                Address             Phone No")
    print("{0:10}{1:20}{2:20}{3:20}".format(contacts[name]["Nickname"], contacts[name]["Name"], contacts[name]["Address"], contacts[name]["Phone Number"]))

def all():
    count = 1
    print("   Nick      Name                Address             Phone No")
    for i in contacts:
        print("{0:0}  {1:10}{2:20}{3:20}{4:20}".format(count, contacts[i]["Nickname"], contacts[i]["Name"], contacts[i]["Address"], contacts[i]["Phone Number"]))
        count += 1


def add():
    while True:
        nickname = input("Enter the nickname: ")
        nickname1 = nickname.title()                        #Capitilising the fisrt letter so that it is case insensitive when using the find function.
        if nickname1 in contacts:
            reply = input("This name already exist, would you like to replace it? (Y)es/(N)o? ")
            if (reply == 'Y') or (reply == 'y'):            #Checking if the name already exist.
                nickname1 = nickname1
            elif (reply == 'N') or (reply == 'n'):
                continue
        name = input("Enter the Name: ")
        name1 = name.title()                                #Capitilising the first letter of each word (just so it looks good when displaying)
        address = input("Enter the Address: ")
        number = input("Enter the phone number: ")
        contacts[nickname1] = {"Nickname": nickname1,"Name": name1,"Address":address, "Phone Number":number}
        display(nickname1)
        break

def delete():
    while True:
        reply = input("Enter the name that you would like to delete: ")
        reply1 = reply.title()
        if (reply1 in contacts):
            answer = input("Are you sure you want to delete {0}? enter (Y)es or (N)o: ".format(reply1))
            if (answer == 'Y') or (answer == 'y'):          #Checking if the name is in the contacts, if so it will ask if you are sure before deleting.
                del contacts[reply1]
                all()
                break
            else:
                print("Returning you to main menu.")
                break
        else:
            print("Error - Could not find name in contacts.")
            reply = input("(C)ontinue\n(R)eturn to main menu: ")
            if (reply == 'R') or (reply == 'r'):
                break

def find():
    while True:
        reply = input("Enter the nickname you would like to search for: ")
        reply1 = reply.title()     #Capiltilising the first letter only so it matches with the address book.
        if (reply1 in contacts):
            display(reply1)
            break
        else:
            print("Error - Could not find name in contacts.")

while True:
    reply = input("\n*** My Contacts ***\n"
          "  (F)ind\n"
          "  (A)dd new entry\n"
          "  (D)elete\n"
          "  (L)ist all\n"
          "  (Q)uit\n"
          "command: ? ")

    if (reply == 'F') or (reply == 'f'):
        find()
    if (reply == 'A') or (reply == 'a'):
        add()
    if (reply == 'D') or (reply == 'd'):
        delete()
    if (reply == 'L') or (reply == 'l'):
        all()
    if (reply == 'Q') or (reply == 'q'):
        print("Program Terminated")
        break