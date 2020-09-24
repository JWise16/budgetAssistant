import random
from os import path, remove
from typing import Optional
from userInfo.singleValue.singleValue import SingleValue


def createID(securityID: str, filePath: str = 'infoData/passwordInfo.txt') -> Optional[SingleValue]:
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


def createNewID(filePath: str = 'infoData/securityIDInfo.txt') -> Optional[SingleValue]:
    """
    creates a SingleValue object for a ID and a new securityID and securityIDInfo
    data file
    :param filePath: path to the password data file
    :return: SingleValue object for a password
    """
    newid = ''
    for i in range(1, 8):
        newid = newid + str(random.randint(1, 9))
    if path.exists(filePath):
        remove(filePath)
    return SingleValue(newid, filePath, 'id', newid)


def getID(singlevalue: SingleValue) -> str:
    """
    :param singlevalue: SingleValue for the id
    :return: the users id
    """
    return singlevalue.data('securityID')
