from loginPage.loginMethods import *


def login() -> dict:
    logging_in = True
    if hasUserInfo():
        while logging_in:
            given_username = str.strip(input("Please enter your username: "))
            given_password = str.strip(input("Please enter your password: "))
            if checkLoginInfo(given_username, given_password):
                print("Logging in...")
                logging_in = False
                pass
            else:
                raise ValueError("Username or password is incorrect")
        user_info = makeUserInfo()
    else:
        print("No login information found, please create an account\n")
        new_username = input("Enter your new username: ")
        new_password = input('Enter your new password: ')
        new_email = input('Enter your email: ')
        user_info = makeNewUserInfo(new_username, new_password, new_email)
        print('Congratulations, your account has been created!\n')

    return user_info
