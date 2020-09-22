from userInfo.singleValue.singleTools.singleTools import terminateProgram
from os import remove


class SingleValue:

    def __init__(self, securityID, path, storage, data):
        """
        This constructor is called if a new data file needs to be created for the SingleValue... calls main constructor
        after making new data file
        :param securityID: user ID
        :param path: path to the new data file
        :param storage: type of data SingleValue will hold
        :param data: the data that SingleValue will hold
        """
        self._info = None
        self.newDataFile(securityID, path, storage, data)
        self.__init__(securityID, path)

    def __init__(self, securityID, path):
        """
        This constructor is always called. Loads information into the self._info tree
        :param securityID: user ID
        :param path: path to the datafile
        """
        with open(path, 'r') as f:
            contents = f.readlines()
            if contents[0] == securityID:
                if len(contents) == 3:
                    self._info = {'id': str(securityID),
                                  'path': str(path),
                                  'type': str(contents[1]),
                                  'data': str(contents[2])}

    def path(self, securityID: str) -> str:
        """
        :param securityID: users ID
        :return: path to data file
        """
        self.idCheck(securityID)
        return self._info['path']

    def type(self, securityID: str) -> str:
        """
        :param securityID:  users ID
        :return: what type of data SingleValue holds
        """
        self.idCheck(securityID)
        return self._info['type']

    def data(self, securityID: str) -> str:
        """
        :param securityID: users ID
        :return: the data SingleValue holds
        """
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
            terminateProgram('Access Denied')

    def newDataFile(self, securityID, path, storage, data) -> None:
        """
        This creates a new data file for the single value
        :param securityID: users securityID
        :param path: path to the file
        :param storage: what kind of data the SingleValue holds
        :param data: the data the SingleValue holds
        :return: None
        """
        with open(path, "w+") as f:
            f.writelines([str(securityID), str(storage), str(data)])
            f.close()

    def removeDataFile(self, securityID) -> None:
        """
        removes the data file
        :param securityID: users ID
        :param path: path to data file
        :return: None
        """
        self.idCheck(securityID)
        remove(self._info['path'])
