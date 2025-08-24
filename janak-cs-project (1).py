import tabulate
print("\n             SCHOOL MANAGEMENT SYSTEM PROGRAM           ")
section9A = []
section9B = []
section9C = []
section10A = []
section10B = []
section10C = []
section11A = []
section11B = []
section11C = []
section12A = []
section12B = []
section12C = []
roll9, roll10, roll11, roll12 = {}, {}, {}, {}
admission_no = {}
class9 = {"9A": section9A, '9B': section9B, "9C": section9C}
class10 = {"10A": section10A, '10B': section10B, "10C": section10C}
class11 = {"11A": section11A, '11B': section11B, "11C": section11C}
class12 = {"12A": section12A, '12B': section12B, "12C": section12C}
school = {'9': class9, '10': class10, '11': class11, '12': class12}
rollschool = {}
admission_count = 1
deletedadmn_list = []
names = []
table1 = [["Admission_no", "Name", "Roll_no", "Father's_name", "Mother's_name", "Mobile_no",
           "Transport_mode"]]
y = False


def remove_add(list_name, position, insertion):
    list_name.remove(list_name[position])
    list_name.insert(position, insertion)


def rollno(k, Class, roll, j):
    c = 1
    for l in j:
        if k.startswith("9"):
            if c < 10:
                roll["0"+k+"0"+str(c)] = l
            else:
                roll["0"+k+str(c)] = l
        elif k.startswith(Class):
            if c < 10:
                roll[k+"0"+str(c)] = l
            else:
                roll[k+str(c)] = l
        c += 1


def key(a, b):
    c = ''
    for i in a:
        if a[i] == b:
            c = i
    return c


def classcall(Class, i):
    if i != []:
        table3 = [["Admission_no", "Name", "Roll_no", "Father's_name", "Mother's_name", "Mobile_no",
                   "Transport_mode"]]
        print(key(Class, i) + ":")
        for j in i:
            roll_no1 = key(rollschool, j)
            admn1 = key(admission_no, j)
            for k in range(len(table1)):
                if j in table1[k]:
                    list3 = [admn1, j, roll_no1, table1[k][3], table1[k][4], table1[k][5], table1[k][6]]
                    table3.append(list3)
                    break
                elif k == len(table1) - 1:
                    list3 = [admn1, j, roll_no1, "-", "-", "-", "-"]
                    table3.append(list3)
        return tabulate.tabulate(table3, tablefmt="outline")


while True:
    print('''\n1.Add new students
2.Add individual student details
3.See data stored
4.See class wise details
5.Search for student
6.Remove student
7.Quit''')
    choice = int(input("Enter your choice (1-7):"))
    z = False
    # Add new students
    if choice == 1:
        z = True
        num = int(input("Enter no of students:"))
        for i in range(num):
            name = input("\nEnter student name:").title()
            names.append(name)
            if names.count(name) == 1:
                Class = input("Enter class:")
                sec = input("Enter section:").upper()
                class_sec = Class+sec
                admission_no[admission_count] = name
                if Class in school:
                    if class_sec in class11:
                        class11[class_sec].append(name)
                        print("Added the student in", class_sec, "with admission no: ", admission_count)
                    elif class_sec in class10:
                        class10[class_sec].append(name)
                        print("Added the student in", class_sec, "with admission no: ", admission_count)
                    elif class_sec in class9:
                        class9[class_sec].append(name)
                        print("Added the student in", class_sec, "with admission no: ", admission_count)
                    elif class_sec in class12:
                        class12[class_sec].append(name)
                        print("Added the student in", class_sec, "with admission no: ", admission_count)
                    else:
                        print('Section not found. enter a section between A to C.')
                        admission_count -= 1
                        names.pop()
                else:
                    print("Class not found.Enter a class between 9 to 12.")
                    admission_count -= 1
                    names.pop()
                admission_count += 1
            else:
                print("Enter an unique name.\n")
                names.pop()

        else:
            print("All students added.")
    # Add individual student details
    elif choice == 2:
        while True:
            print("Enter the following details-")
            lc = int(input("Admission No:"))
            Name = input("Student Name:").title()
            x = True
            if lc <= len(admission_no) and not lc == 0:
                if admission_no[lc] == Name:
                    for i in range(len(table1)):
                        if lc == table1[i][0]:
                            choice2 = input("Do you want to overwrite the details?:").title()
                            if choice2 == "Yes":
                                father_name = input("Father's Name:").title()
                                remove_add(table1[i], 3, father_name)
                                mother_name = input("Mother's Name:").title()
                                remove_add(table1[i], 4, mother_name)
                                mobile_no = int(input("Mobile No:"))
                                remove_add(table1[i], 5, mobile_no)
                                transport_mode = input("Mode of Transport:").title()
                                remove_add(table1[i], 6, transport_mode)
                            else:
                                print("Chose not to overwrite.")
                                break
                            x = False
                    else:
                        if x:
                            father_name = input("Father's Name:").title()
                            mother_name = input("Mother's Name:").title()
                            mobile_no = int(input("Mobile No:"))
                            transport_mode = input("Mode of Transport:").title()
                            roll_no = key(rollschool, admission_no[lc])
                            list1 = [lc, Name, roll_no, father_name, mother_name, mobile_no,
                                     transport_mode]
                            table1.append(list1)
                    y = True
                    break
                else:
                    print("Admission number is not matching with the name. Please recheck and Enter.")
            elif lc == 0:
                break
            else:
                print("Enter proper Admission number.")
    # See data stored
    elif choice == 3:
        if admission_no != {}:
            choice1 = input("Do you want to see the details of individual student? ")
            if choice1 != 'yes':
                lc = 1
                table2 = [['Admission_no', "Name", "Class", "section", "Roll no"]]
                while lc < admission_count:
                    if lc not in deletedadmn_list:
                        roll_no = key(rollschool, admission_no[lc])
                        list2 = [lc, admission_no[lc], roll_no[0:2], roll_no[2], roll_no]
                        table2.append(list2)
                    else:
                        list2 = ["-", "-", "-", "-", "-"]
                        table2.append(list2)
                    lc += 1
                print(tabulate.tabulate(table2, tablefmt="outline"))
            elif y:
                print(tabulate.tabulate(table1, tablefmt="outline"))
            else:
                print("No details added.")
        else:
            print("No student found.")
    # See classwise details
    elif choice == 4:
        choice1 = int(input("\nFor which class would you like to see the details of:"))
        if choice1 == 9:
            for i in class9.values():
                a = (classcall(class9, i))
                if a != None:
                    print(a)
        elif choice1 == 10:
            for i in class10.values():
                a = (classcall(class10, i))
                if a != None:
                    print(a)
        elif choice1 == 11:
            for i in class11.values():
                a = (classcall(class11, i))
                if a != None:
                    print(a)
        elif choice1 == 12:
            for i in class12.values():
                a = (classcall(class12, i))
                if a != None:
                    print(a)
        else:
            print("Enter class between 9-12.")
    # Search student
    elif choice == 5:
        name = input("\nEnter student name: ").title()
        if name in rollschool.values():
            print("Student is a part of the school.")
            rol = key(rollschool, name)
            for i in range(len(table1)):
                u = True
                if name in table1[i]:
                    print(tabulate.tabulate([["admission_no", "Name", "Roll_no", "father's_name",
                                              "mother's_name", "mobile_no", "Transport_mode"], table1[i]],
                                            tablefmt="outline"))
                    u = False
                elif i == len(table1)-1 and u:
                    print(tabulate.tabulate([["admission_no", "Name", "Class", "Section", "Roll_no"],
                    [key(admission_no, name), name, rol[0:2], rol[2], rol]], tablefmt="outline"))
        else:
            print("Student is not a part of the school.")
    # Delete a student
    elif choice == 6:
        print(admission_no)
        name = input("Enter name of the student to be deleted:").title()
        if name in admission_no.values():
            admn = key(admission_no, name)
            print("Is the admission no of the student", key(admission_no, name), end=" ")
            c2 = input()
            c3 = input("Are you sure you want to delete this student:")
            if (c2 == "yes") and (c3 == "yes"):
                del admission_no[admn]
                roll = key(rollschool, name)
                del rollschool[roll]
                for i in school.values():
                    for j in i.values():
                        if name in j:
                            j.remove(name)
                if y:
                    for i in table1:
                        if i[0] == admn:
                            table1.remove(i)
                print("Student deleted.")
                deletedadmn_list.append(admn)
                z = True
            else:
                print("Try again.")
        else:
            print("Student is already not a part of the school.")
    # Quit
    elif choice == 7:
        print("WARNING data entered will be lost ")
        c = input("Do you still want to quit(yes/no):")
        if c == 'yes':
            print("Quiting program,goodbye!")
            break
        else:
            print("Quiting cancelled continuing the program.")
    else:
        print("Choose proper number.")
    # Roll no assignment
    if z:
        for i in school.values():
            for j in i.values():
                if j != []:
                    j.sort()
                    k = key(i, j)
                    rollno(k, "9", roll9, j)
                    rollno(k, "10", roll10, j)
                    rollno(k, "11", roll11, j)
                    rollno(k, "12", roll12, j)
        rollschool.update(roll9)
        rollschool.update(roll10)
        rollschool.update(roll11)
        rollschool.update(roll12)
