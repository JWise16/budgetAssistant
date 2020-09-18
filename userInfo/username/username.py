"""
functions that work with usernameInfo.txt
"""
import sys


# work in progress
def getEmail(key) -> str:
    """
    This function checks the users access key and returns the email of the user
    :param key: users access key
    :return: email of the user
    """
    header = 1234
    if key == header:
        # get the email from the email file
        pass
    else:
        sys.exit("Access Denied")
    return ""


# work in progress
def changeEmail(key, newEmail) -> None:
    pass


# work in progress
def removeEmail(key) -> None:
    pass
