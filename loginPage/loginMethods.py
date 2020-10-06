from os import path
from userInfo import email, password, purchase, savings, securityID, username, work
import csv


# TODO: Make method to create securityID

def checkLoginInfo(username: str, password: str) -> bool:
    if path.exists("../userInfo/singleValue/infoData/usernameInfo.csv"):
        with open("../userInfo/singleValue/infoData/usernameInfo.csv", 'r') as f:
            reader = csv.reader(f)
            id = str.rstrip(next(reader)[0])
            storage = str.rstrip(next(reader)[0])
            data = str.rstrip(next(reader)[0])
            if data != username:
                print("Incorrect username")
                return False
    else:
        print("No username file found")
        return False

    if path.exists("../userInfo/singleValue/infoData/passwordInfo.csv"):
        with open("../userInfo/singleValue/infoData/passwordInfo.csv", 'r') as f:
            reader = csv.reader(f)
            id = str.rstrip(next(reader)[0])
            storage = str.rstrip(next(reader)[0])
            data = str.rstrip(next(reader)[0])
            if data != password:
                print("Incorrect password")
                return False
    else:
        print("No password file found")
        return False

    return True


def hasUserInfo() -> bool:
    if not path.exists("../userInfo/singleValue/infoData/emailInfo.csv"):
        print("No email information")
        return False
    if not path.exists("../userInfo/singleValue/infoData/usernameInfo.csv"):
        print("No username information")
        return False
    if not path.exists("../userInfo/singleValue/infoData/passwordInfo.csv"):
        print("No password information")
        return False
    if path.exists("../userInfo/singleValue/infoData/securityIDInfo.csv") is False:
        print("No ID information")
        return False
    if not path.exists("../userInfo/tableValue/tableData/purchaseInfo.csv"):
        print("No purchase information")
        return False
    if not path.exists("../userInfo/tableValue/tableData/savingsInfo.csv"):
        print("No savings information")
        return False
    if not path.exists("../userInfo/tableValue/tableData/workInfo.csv"):
        print("No work information")
        return False
    return True


def makeNewUserInfo(new_username: str, new_password: str, new_email: str) -> dict:
    user_info = dict()
    user_info['ID'] = securityID.getID(securityID.createNewID())
    user_info['Email'] = email.createNewEmail(user_info['ID'], new_email)
    user_info['Password'] = password.createNewPassword(user_info['ID'], new_password)
    user_info['Username'] = username.createNewUsername(user_info['ID'], new_username)
    user_info['Purchase'] = purchase.createNewPurchaseHistory(user_info['ID'])
    user_info['Work'] = work.createNewWorkLog(user_info['ID'])
    user_info['Savings'] = savings.createNewSavings(user_info['ID'])
    return user_info


def makeUserInfo() -> dict:
    user_info = dict()
    user_info['ID'] = securityID.getID(securityID.createID("securityID"))
    user_info['Email'] = email.createEmail(user_info['ID'])
    user_info['Password'] = password.createPassword(user_info['ID'])
    user_info['Username'] = username.createUsername(user_info['ID'])
    user_info['Purchase'] = purchase.createPurchaseHistory(user_info['ID'])
    user_info['Work'] = work.createWorkLog(user_info['ID'])
    user_info['Savings'] = savings.createSavings(user_info['ID'])
    return user_info
