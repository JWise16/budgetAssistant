from userInfo.singleValue.singleTools.singleTools import checkAndCreateFile

"""
functions that work with securityIDInfo.txt
"""


# TODO: finish ID implementation
# work in progress
def getID(key) -> str:
    """
       This function returns the ID of the user
       :param key: users access key
       :return: username of the user
       """
    if True:
        # get the ID from the securityIDInfo file
        return ''
    else:
        raise SystemExit(0)


# work in progress
def setupID() -> None:
    checkAndCreateFile("key")
    # create & upload 8 digit ID


# work in progress
def idCheck(key, path) -> bool:
    return key == 'key'
