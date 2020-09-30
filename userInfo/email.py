from os import path
from typing import Optional
from userInfo.singleValue.singleValue import SingleValue

"""
functions that work with emailInfo.csv
"""


def createEmail(securityID: str, filePath: str = 'userInfo/singleValue/infoData/emailInfo.csv') -> object:
    """
    creates a SingleValue object for a email from an exiting email
    data file
    :param securityID: users ID
    :param filePath: path to the email data file
    :return: SingleValue object for a email or None if a data file is not found
    """
    if path.exists(filePath):
        return SingleValue(securityID, filePath)
    else:
        print('Data File Does not exist for email... Please call createNewEmail()')
        return None


def createNewEmail(securityID: str, email: str, filePath: str = 'userInfo/singleValue/infoData/emailInfo.csv') -> \
        Optional[SingleValue]:
    """
    creates a SingleVale object for a username and creates a new
    username data file
    :param securityID: users ID
    :param email: the users email
    :param filePath: path to the email information file
    :return: SingleValue object for a username or call createEmail() if a data file is already found
    """
    if not path.exists(filePath):
        return SingleValue(securityID, filePath, 'email', email)
    else:
        print('Data file already exists for email... calling createEmail()')
        createEmail(securityID, filePath)


def getEmail(securityID: str, singlevalue: SingleValue) -> str:
    """
    :param securityID: users ID
    :param singleValue: SingleValue for the email
    :return: the email
    """
    return str(singlevalue.data(securityID))


def changeEmail(securityID: str, newEmail: str, singlevalue: SingleValue) -> None:
    """
    changes the email
    :param securityID: users ID
    :param newEmail: the new email
    :param singlevalue: SingleValue for the email
    :return: None
    """
    singlevalue.changeInfo(securityID, 'data', newEmail)
