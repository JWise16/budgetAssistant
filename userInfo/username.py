from os import path
from typing import Optional
from userInfo.singleValue.singleValue import SingleValue

"""
functions that work with usernameInfo.txt
"""


def createUsername(securityID: str, filePath: str = '../userInfo/singleValue/infoData/usernameInfo.csv') -> object:
    """
    creates a SingleValue object for a username from an exiting username
    data file
    :param securityID: users ID
    :param filePath: path to the username data file
    :return: SingleValue object for a username or None if a data file is not found
    """
    if path.exists(filePath):
        return SingleValue(securityID, filePath)
    else:
        print('Data File Does not exist for username... Please call createNewUsername()')
        return None


def createNewUsername(securityID: str, username: str,
                      filePath: str = '../userInfo/singleValue/infoData/usernameInfo.csv') -> Optional[
    SingleValue]:
    """
    creates a SingleVale object for a username and creates a new
    username data file
    :param securityID: users ID
    :param username: the users username
    :param filePath:
    :return: SingleValue object for a username or call createUsername() if a data file is already found
    """
    if not path.exists(filePath):
        return SingleValue(securityID, filePath, 'username', username)
    else:
        print('Data file already exists for  username... calling create username()')
        createUsername(securityID, filePath)


def getUsername(securityID: str, singlevalue: SingleValue) -> str:
    """
    :param securityID: users ID
    :param singlevalue: SingleValue for the username
    :return: the username
    """
    return str(singlevalue._data(securityID))


def changeUsername(securityID: str, newUsername: str, singlevalue: SingleValue) -> None:
    """
    changes the  username
    :param securityID: users ID
    :param newUsername: the new username
    :param singlevalue: SingleValue for the username
    :return: None
    """
    singlevalue._changeInfo(securityID, 'data', newUsername)
