from os import path
from typing import Optional
from userInfo.singleValue.singleValue import SingleValue

"""
functions that work with passwordInfo.txt
"""


def createPassword(securityID: str, filePath: str = 'userInfo/singleValue/infoData/passwordInfo.txt') -> Optional[
    SingleValue]:
    """
    creates a SingleValue object for a password from an exiting password
    data file
    :param securityID: users ID
    :param filePath: path to the password data file
    :return: SingleValue object for a password or None if a data file is not found
    """
    if path.exists(filePath):
        return SingleValue(securityID, filePath)
    else:
        print('Data File Does not exist for password... Please call createNewPassword()')
        return None


def createNewPassword(securityID: str, password: str,
                      filePath: str = 'userInfo/singleValue/infoData/passwordInfo.txt') -> Optional[
    SingleValue]:
    """
    creates a SingleVale object for a password and creates a new
    password data file
    :param securityID: users ID
    :param password: the users password
    :param filePath: path to the password information file
    :return: SingleValue object for a password or call createPassword() if a data file is already found
    """
    if not path.exists(filePath):
        return SingleValue(securityID, filePath, 'password', password)
    else:
        print('Data file already exists for email... calling createPassword()')
        createPassword(securityID, filePath)


def getPassword(securityID: str, singlevalue: SingleValue) -> str:
    """
    :param securityID: users ID
    :param singlevalue: SingleValue for the password
    :return: the password
    """
    return str(singlevalue.data(securityID))


def changePassword(securityID: str, newPassword: str, singlevalue: SingleValue) -> None:
    """
    changes the password
    :param securityID: users ID
    :param newPassword: the new password
    :param singlevalue: SingleValue for the password
    :return: None
    """
    singlevalue.changeInfo(securityID, 'data', newPassword)
