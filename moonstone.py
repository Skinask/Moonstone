import requests

def check_account(email, password):
    url = "https://api.moonton.com/v1/account/login"
    data = {
        "email": email,
        "password": password
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            if "verification_code" in response.text:
                return "NO"
            else:
                return "YES"
        else:
            return "Error: " + str(response.status_code)
    except Exception as e:
        return "Error: " + str(e)

def main():
    email = input("Enter email: ")
    password = input("Enter password: ")
    result = check_account(email, password)
    print(result)

if __name__ == "__main__":
    main()
