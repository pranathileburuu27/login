def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        print("Login Successful!")
        return True
    else:
        print("Invalid Username or Password")
        return False


if __name__ == "__main__":
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")
    login(user, pwd)
