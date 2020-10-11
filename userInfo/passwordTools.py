from os import path
from typing import Optional
from userInfo.singleValue.singleValue import SingleValue

"""
functions that work with passwordInfo.txt
"""

def loadPassword(securityID: str, filePath: str = '../userInfo/singleValue/infoData/passwordInfo.csv') -> Optional[
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


def createNewPassword(securityID: str, new_password: str,
                      filePath: str = '../userInfo/singleValue/infoData/passwordInfo.csv') -> Optional[
    SingleValue]:
    """
    creates a SingleVale object for a password and creates a new
    password data file
    :param securityID: users ID
    :param new_password: the users password
    :param filePath: path to the password information file
    :return: SingleValue object for a password or call loadPassword() if a data file is already found
    """
    if not path.exists(filePath):
        return SingleValue(securityID, filePath, 'password', new_password)
    else:
        print('Data file already exists for password... calling loadPassword()')
        loadPassword(securityID, filePath)


def getPassword(securityID: str, singlevalue: SingleValue) -> str:
    """
    :param securityID: users ID
    :param singlevalue: SingleValue for the password
    :return: the password
    """
    return str(singlevalue._data(securityID))


def changePassword(securityID: str, new_password: str, singlevalue: SingleValue) -> None:
    """
    changes the password
    :param securityID: users ID
    :param new_password: the new password
    :param singlevalue: SingleValue for the password
    :return: None
    """
    singlevalue._changeInfo(securityID, 'data', new_password)
