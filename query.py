import paramiko


class SMTH():
    def smth(self):
        x = input("Enter Payment Secret Code: ")
        if x == "PAYMENT_DONE":
            return True
        else:
            return False


trial = 0
while trial < 5:
    y = SMTH().smth()
    if y == True:
        print("Payment Has been made successfully")
        usr = "Irwin"
        pas = "Raspberry"
        ip = "192.168.137.234"
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(ip, username=usr, passphrase=pas)
        ssh.exec_command(f"python3 ~/Projects/Host.py")
        ssh.close()

        break
    else:
        print("Invalid Code, Try again ("+str(4-trial)+" trials left)")
        if trial == 4:
            print("Maximum Number of Attempts Reached")
            break
        trial += 1
else:
    exit(1)
