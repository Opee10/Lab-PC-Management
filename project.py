def AddPc():
    pc_num = input("Enter PC number: ")
    os_installed = input("Enter OS installed: ")
    status = input("Enter PC status: ")
    pc = [pc_num, os_installed, status]
    if pc_num in dic.keys():
        print("This PC is exists!")
        choice = input("Do you want to modify or remove (M/R): ")
        if choice == "M":
            UpdatePc(pc_num)
        elif choice == "R":
            RemovePc(pc_num)
        else:
            pass
    else:
        dic[pc_num] = pc
        print("PC added successfully!")

def UpdatePc(pc_num):
    os_installed = input("Enter new OS installed: ")
    status = input("Enter new status: ")
    dic[pc_num] = [pc_num, os_installed, status]
    print("PC information updated successfully..")

def RemovePc(pc_num):
    del dic[pc_num]
    print("PC removed successfully!")

def AllPcsDisplay():
    print("PC Number\tOS Installed\tStatus")
    for pc in dic.values():
        print(f"{pc[0]}\t\t\t{pc[1]}\t\t\t{pc[2]}")

def DisplayPc(pc_num):
    if pc_num in dic.keys():
        pc = dic[pc_num]
        print(f"PC Number: {pc[0]}")
        print(f"OS Installed: {pc[1]}")
        print(f"Status: {pc[2]}")
    else:
        print("PC not found!")

def SearchPc():
    pc_num = input("Enter PC number: ")
    if pc_num in dic.keys():
        DisplayPc(pc_num)
    else:
        choice = input("PC not found! Do you want to add this PC? (y/n): ")
        if choice == "y":
            AddPc()

def StorePcs():
    with open("pcs.txt", 'w') as f:
        f.write("PC Number\tOS Installed\tStatus\n")
        for pc in dic.values():
            f.write(f"{pc[0]}\t\t{pc[1]}\t\t{pc[2]}\n")
    print("PC information stored to file successfully!")

def Display():
    global dic
    dic = {}
    while True:
        print("\nLab PC Management system\n")
        print("1. Add PC")
        print("2. Update PC functionality")
        print("3. Remove PC")
        print("4. Display all PCs Information")
        print("5. Display an Individual PCs information")
        print("6. Search existing PC")
        print("7. Store PCs Information to file")
        print("8. Quit operation")
        choice = input("\nEnter an operation: ")
        
        if choice == "1":
            AddPc()
        elif choice == "2":
            pc_num = input("Enter PC number to update: ")
            UpdatePc(pc_num)
        elif choice == "3":
            pc_num = input("Enter PC number to remove: ")
            RemovePc(pc_num)
        elif choice == "4":
            AllPcsDisplay()
        elif choice == "5":
            pc_num = input("Enter PC number to display: ")
            DisplayPc(pc_num)
        elif choice == "6":
            SearchPc()
        elif choice == "7":
            StorePcs()
        else:
            exit()

o1 = Display()
