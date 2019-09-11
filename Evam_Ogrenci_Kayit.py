import os

"""Student Information Program"""

def menu():
    print("Student Information Table")
    print()
    print("*** With this program, you can register, list, update and delete new students. ***")
    print()
    print("1- Register New Student")
    print("2- Lists")
    print("3- Update")
    print("4- Delete")
    print("5- Exit")
    print()

    while True:
        try:
           user_selection = int(input("Select the action you want to make:"))
           return user_selection
        except ValueError as Failed:
            print("Invalid Selection !!!")
            continue

def register():
    save = True
    while save:
        with open("data.txt","a") as stu_file:
            print("--Register New Student--")
            no    = input("Student Number:")
            name = input("Student Name:")
            surname = input("Student Surname:")
            print("Registration Completed")
            Inf_Register = "{:12}\t{:15}\t{:15}\n".format(no,name,surname)
            stu_file.write(Inf_Register)
            new_reg = input("Would you like to make a new register?  (Y/N):")
            if new_reg.lower() == 'y':
                save = True
            else:
                print("Returning to the menu")
                save = False
                print()
def lists():
    print("--Lists--")
    folder = open("data.txt","r")
    print(folder.read())


def update():
    print("--Update--")
    print("---which would you like to update?---")
    print("1- Student number to update")
    print("2- Student name to update")
    print("3- Student surname to update")
    print()
    upd_selection = int(input("Select the action you want to make:"))

    if upd_selection == 1:
        stu_no = input("Student number to update:")
        old_stu_file = open("data.txt","r") # eski dosyayı okuyoruz
        new_stu_file = open("new.txt","w") # yeni dosyaya yazıyoruz
        for j in old_stu_file:
            lines = j.split("\t") # arasında tab olan kelimeleri ayırıyoruz. ve j ile bu kelimeleri bir bir alıyoruz.
            if lines[0].strip() == stu_no.strip(): # eski dosyadaki no ile güncellenmek istenilen no aynı ise şunları yap.
                new_stu_no = input("New student number:")
                new_stu_file.write(new_stu_no + "\t" + lines[1] + "\t" + lines[2])
                print("Update completed")
                continue
            else:
                new_stu_file.write(j)
        old_stu_file.close()
        new_stu_file.close()
        os.remove("./data.txt")
        os.rename("./new.txt", "data.txt")

    elif upd_selection == 2:
        stu_name = input("Student name to update:")
        old_stu_file = open("data.txt","r")
        new_stu_file = open("new.txt","w")
        for k in old_stu_file:
            lines = k.split("\t")
            if lines[1].strip() == stu_name.strip():
                new_stu_name = input("New student name:")
                new_stu_file.write(lines[0] + "\t" + new_stu_name + "\t" + lines[2])
                print("Update completed")
                continue
            else:
                new_stu_file.write(k)
        old_stu_file.close()
        new_stu_file.close()
        os.remove("./data.txt")
        os.rename("./new.txt", "data.txt")

    elif upd_selection == 3:
        stu_surname = input("Student surname to update:")
        old_stu_file = open("data.txt","r")
        new_stu_file = open("new.txt","w")
        for l in old_stu_file:
            lines = l.split("\t")
            if lines[2].strip() == stu_surname.strip():
                new_stu_surname = input("New student surname:")
                new_stu_file.write(lines[0] + "\t" + lines[1] + "\t" + new_stu_surname)
                print("Update completed")
                continue
            else:
                new_stu_file.write(l)
        old_stu_file.close()
        new_stu_file.close()
        os.remove("./data.txt")
        os.rename("./new.txt", "data.txt")

def delete():
    print("--Delete--")
    stu_no = input("Student number to be deleted:")
    old_stu_file = open("data.txt", "r")
    new_stu_file = open("new.txt", "w")

    for k in old_stu_file:
        lines = k.split("\t")
        if lines[0].strip() == stu_no.strip():
            print("Unregister completed")
            continue
        else:
            new_stu_file.write(k)

    old_stu_file.close()
    new_stu_file.close()
    os.remove("./data.txt")
    os.rename("./new.txt", "data.txt")
    print()

def exit():
    print("---Goodbye---")
    quit()


go = True
while go:
    user_selection = menu()
    if   user_selection == 1:
        register()
    elif user_selection == 2:
        lists()
    elif user_selection == 3:
        update()
    elif user_selection == 4:
        delete()
    elif user_selection == 5:
        exit()
