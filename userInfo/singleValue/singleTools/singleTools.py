from userInfo.singleValue.singleValue import SingleValue


def createInfo(securityID, path) -> SingleValue:
    """
    creates a SingleValue object from an existing data file
    :param securityID: users ID
    :param path: path to the existing data file
    :return: SingleValue object
    """
    return SingleValue(securityID, path)


def createNewInfo(securityID, path, storage, data) -> SingleValue:
    """
    creates a SingleValue object and a data file for the SingleValue
    :param securityID: users ID
    :param path: path to new data file
    :param storage: type of data the SingleValue will be storing
    :param data:
    :return:
    """
    return SingleValue(securityID, path, storage, data)


def getData(securityID, singlevalue: SingleValue) -> str:
    """
    returns the information associated with the
    :param securityID: users ID
    :param singlevalue: SingleValue object to get data from
    :return: data SingleValue holds
    """
    return singlevalue.getTag(securityID, "data")


def changeInfo(securityID, singlevalue: SingleValue, tag, newData) -> None:
    """
    replaces the old data associated with 'tag' with 'newData'
    :param securityID: users ID
    :param singlevalue: SingleValue object
    :param tag: information to be changed
    :param newData: data to replace the data associated with tag
    :return: None
    """
    singlevalue.changeInfo(securityID, tag, newData)


def terminateProgram(errorMessage=None) -> None:
    """
    This function is called whenever the program needs to terminate
    :param errorMessage: optional error message to be displayed
    :return: No return type
    """
    if errorMessage is 'Access Denied':
        print("Access has been denied... terminating now")
        raise SystemExit(0)
    elif errorMessage is not None:
        print("An Error has occurred in the program\nError Message:", errorMessage + '\nTerminating Now...')
        raise SystemExit(0)
    else:
        print("An Error has occurred in the program\nError Message:", errorMessage + '\nTerminating Now...')
        raise SystemExit(0)
