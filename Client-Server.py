import os
import sys
from cryptography.fernet import Fernet

global reg_updater, reg_time
reg_updater = 0
reg_time = 0
global reg_name, reg_uid
reg_name = ''
reg_uid = ''

def decrypt_data(key, data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(data).decode()
    return decrypted_data


class Main_Menu():
    def main_menu(self):
        print("\n----Tech-Driven Mobility Platform----\n")
        print("Choose one of the following operations (Just type the index of the desired operation): ")
        print('''
        1. Register Yourself
        2. Available Bicycles
        3. Exit
        ''')
        choice = int(input("Your Choice: "))
        os.system("cls")
        if choice == 1:
            Registration().register()
        elif choice == 2:
            Bicycles().cycles()
        elif choice == 3:
            os.system("exit")
        else:
            print("Invalid Choice")


class Registration():
    def register(self):
        global reg_updater, reg_name, reg_uid
        print("\n----Tech-Driven Mobility Platform----\n")
        name = input("Enter your name: ")
        uid = input("Enter a UID of yours (Roll No. given by IITJ): ")
        uid = uid.upper()
        file = open("./Registrations.txt", "r+")
        marker = 0
        i = 0
        for lines in file:
            word = lines.split()
            i += 1
            if uid in word:
                print("Hello, "+name+", you have been registered successfully, please proceed to see available bicycles.")
                marker += 1
        if marker == 0:
            file.write(str(int(i/2)+1)+". Name: "+name+"\n   UID: "+uid+"\n")
            print("Hello, " + name + ", you are registered successfully, please proceed to see available bicycles.")
        file.close()
        proceed = input("Do you wish to proceed(y or n): ")
        if proceed == 'y' or proceed == 'Y':
            os.system("cls")
            reg_updater += 1
            reg_name += name
            reg_uid += uid
            Bicycles().cycles()
        else:
            Main_Menu().main_menu()


class Bicycles(Registration):
    def cycles(self):
        print("\n----Tech-Driven Mobility Platform----\n")
        print("Price: Rs.100/hour for each bicycle")
        print("1. Cycle-A")
        print("2. Cycle-B")
        print("3. Cycle-C")
        print("4. Cycle-D")
        print("5. Cycle-E")
        cycle_choice = int(input("Enter the index of your desired bicycle: "))
        if cycle_choice <= 5:
            if reg_updater == 0:
                print("Register Yourself")
                Registration().register()
            else:
                print("Bicycle choice", cycle_choice, "has been chosen, proceed for Payment")
        else:
            print("Invalid Choice")
        proceed = input("Do you wish to proceed(y or n): ")
        if proceed == 'y' or proceed == 'Y':
            os.system("cls")
            Payment().pay()
        else:
            Main_Menu().main_menu()


class Payment():
    def pay(self):
        global reg_time
        print("\n----Tech-Driven Mobility Platform----\n")
        print("Price: Rs.100/hour for each bicycle")
        time = float(input("Enter the duration (in hours) for which you wish to rent the bicycle: "))
        reg_time += time
        print("Total Rent: Rs.", 100*time)
        print("GST: Rs.", 5*time)
        print("Amount to be paid: Rs.", 105*time)
        proceed = input("Do you wish to proceed(y or n): ")
        if proceed == 'y' or proceed == 'Y':
            os.system("cls")
            Payment().query()
        else:
            Main_Menu().main_menu()

    def query(self):
        print("\n----Tech-Driven Mobility Platform----\n")
        print("Confirm Your Name and UID:")
        print("Name: "+reg_name+"\nUID: "+reg_uid)
        x = input("Press 1 to confirm (Press any other key to change): ")
        if x == '1':
            print("Username and UID has been confirmed, kindly make the required payment: ")
            print("Total Rent: Rs.", 100 * reg_time)
            print("GST: Rs.", 5 * reg_time)
            print("Amount to be paid: Rs.", 105 * reg_time)
            os.system("python ./query.py")
            if len(sys.argv) != 3:
                sys.exit(1)
            key = sys.argv[1]
            data = sys.argv[2]
            passkey = decrypt_data(key, data)
            print(passkey)
        else:
            os.system("cls")
            Registration().register()



if __name__=="__main__":
    os.system("cls")
    Main_Menu().main_menu()
