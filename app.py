addMore = 0

while addMore == 0:
    file = open("datafile.txt", "a")
    exists = False
    name = contact = ''
    while name == '':
        name = input("Username: ")
    while contact == '':
        contact = input("Contact: ")

    name = name.upper()
    contact = contact.upper()
    with open("datafile.txt", "r") as f:
        for line in f:
            line = line.split(' - ')
            if name == line[0] or contact == line[1]:
                line[1] = line[1].strip("\n")
                print("~~~~~~~~~~\nName: " + line[0] + "\nContact: " + line[1] + "\n~~~~~~~~~~")
                exists = True

    strAdd = "Try"
    if exists is not True:
        file.write("\n" + name + " - " + contact)
        strAdd = "Add"
        print("Added to list\n")

    file.close()

    add = ""
    while add != 'Y' and add != 'N' and add != 'PASS':
        add = input(strAdd + " another one (Y/N)? ")
        add = add.upper()

    if add == 'N':
        addMore = 1
    elif add == 'PASS':
        addMore = 99

if addMore == 99:
    file = open("datafile.txt", "w")
    file.truncate(0)
    file.write("TEST - TEST")
    file.close()
    print("Emptied...\n")
    addMore = 1
if addMore == 1:
    print("Exiting...")
    exit(0)
