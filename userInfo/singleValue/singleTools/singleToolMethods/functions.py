# TODO: Clean up singleToolMethods/functions.py

# work in progress
def validFile(key, path) -> bool:
    """
    This function checks to see if a file exists and creates one if it doesn't
    :return: No return type
    """
    try:
        fhandle = open(path, 'r')
        idCheck(key, path)
    except OSError as e:
        print(e)
        return False

    pass
    # if fileExists:
    #   if fileHasHeader:
    #       if checkHeader:
    #           pass
    #       else:
    #           raise SystemExit(0)
    #   else:
    #       setFileHeader to key
    # else:
    #   create info file w/ file header as key


def createStorageFile(key, path, name, info, ) -> None:
    pass


# work in progress
def isValidFilePath(path) -> bool:
    return path == 'path'
