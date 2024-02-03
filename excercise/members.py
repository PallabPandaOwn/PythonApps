file = open("members.txt", "r")
user = file.readlines()
print("Existing Users :-")
for u in user:
    print(u)
file.close()
while True:
    Ask = input("Would you like to add new members? Y/N : ")
    match Ask:
        case "Y":
            member = input("enter new member name: ") + '\n'
            user.append(member)
            file = open("members.txt", "w")
            file.writelines(user)
            file.close()
        case "N":
            print("Thank you for using" + '\n')
            print("List of Members -: ")
            file = open("members.txt", "r")
            user = file.readlines()
            for u in user:
                print(u)
            file.close()
            break
        case _:
            print("Invalid")
