from os import remove


class SingleValue:

    def __init__(self, securityID: str, path: str, storage: str = None, data: str = None):
        """
        Creates new SingleValue object from a existing data file or creates a new data file
        :param securityID:
        :param path:
        :param storage:
        :param data:
        """
        self._info = None
        if storage is not None and data is not None:
            self.newDataFile(securityID, path, storage, data)

        with open(path, 'r') as f:
            id = str.rstrip(f.readline())
            type = str.rstrip(f.readline())
            dat = str.rstrip(f.readline())
            self._info = {'id': id,
                          'path': str(path),
                          'type': type,
                          'data': dat}

    def path(self, securityID: str) -> str:
        """
        :param securityID: users ID
        :return: path to data file
        """
        if self._info['type'] != 'id':
            self.idCheck(securityID)
        return self._info['path']

    def type(self, securityID: str) -> str:
        """
        :param securityID:  users ID
        :return: what type of data SingleValue holds
        """
        if self._info['type'] != 'id':
            self.idCheck(securityID)
        return self._info['type']

    def data(self, securityID: str) -> str:
        """
        :param securityID: users ID
        :return: the data SingleValue holds
        """
        if self._info['type'] != 'id':
            self.idCheck(securityID)
        return self._info['data']

    def changeInfo(self, securityID, tag, newData) -> None:
        """
        This function changes the information in the "self._info" tree... Does not change the actual data file
        :param securityID: users ID
        :param tag: which element of the tree is going to be changed
        :param newData: the new data to be inserted in the tag
        :return:
        """
        if self._info['type'] != 'id':
            self.idCheck(securityID)
        if self._info[tag] is not None:
            self._info[tag] = newData
            print('{tag} was changed to {data}'.format(tag=tag, data=newData))
        else:
            raise ValueError("{thistag} was not found in \'info\'".format(thistag=tag))

    def idCheck(self, securityID) -> bool:
        """
        This function checks to see if the securityID is equal to the SingleValue id
        and terminates the program if it isn't
        :param securityID: users ID
        :return: True if security ID == self._info['id']
        """
        if securityID == self._info['id']:
            return True
        else:
            self.terminateProgram('Access Denied')

    # TODO: make working method to create data files
    def newDataFile(self, securityID, path, storage, data) -> None:
        """
        This creates a new data file for the single value
        :param securityID: users securityID
        :param path: path to the file
        :param storage: what kind of data the SingleValue holds
        :param data: the data the SingleValue holds
        :return: None
        """
        with open(path, 'w+') as f:
            f.writelines(str(securityID))
            f.writelines("\n" + str(storage))
            f.writelines("\n" + str(data))
            f.close()

    def removeDataFile(self, securityID, path) -> None:
        """
        removes the data file
        :param securityID: users ID
        :param path: path to data file
        :return: None
        """
        if self._info['type'] != 'id':
            self.idCheck(securityID)
        remove(self._info['path'])

    def terminateProgram(self, errorMessage=None) -> None:
        """
        This function is called whenever the program needs to terminate
        :param errorMessage: optional error message to be displayed
        :return: No return type
        """
        if errorMessage == 'Access Denied':
            print("Access has been denied... terminating now")
            raise SystemExit(0)
        elif errorMessage is not None:
            print("An Error has occurred in the program\nError Message:", errorMessage + '\nTerminating Now...')
            raise SystemExit(0)
        else:
            print("An Error has occurred in the program\nError Message:", errorMessage + '\nTerminating Now...')
            raise SystemExit(0)
