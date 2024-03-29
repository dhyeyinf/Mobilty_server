import random
import paramiko
from cryptography.fernet import Fernet


def send_encrypted_data(ssh, data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())

    ssh.exec_command(f"python3 ~/Projects/Client-Server.py {key} {encrypted_data}")


def main():
    n = random.randint(1000, 9999)
    usr = "Irwin"
    pas = "Raspberry"
    ip = "192.168.137.114"
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(ip, username=usr, passphrase=pas)

    data = f"Thanks for the purchase\n{n} is your passkey for the chosen bicycle"

    send_encrypted_data(ssh, data)
    ssh.close()

if __name__=="__main__":
    main()
