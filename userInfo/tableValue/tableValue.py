from userInfo.singleValue.singleValue import SingleValue


class TableValue(SingleValue):

    def __init__(self, securityID: str, path: str, storage: str = None, data: str = None, dataPath: str = None):
        super().__init__(securityID, path, storage, "tableData")
        # add table data into self._info
        # add data table path to self._info

    def datapath(self, securityID) -> None:
        # return the data path from self._info
        pass

    def addEntry(self, date: str, amount: str, reason: str, tag: str = None) -> None:
        # pandas code to append an entry onto a data table
        pass

    # work in progress
    def removeEntry(self, securityID: str, entryID: str) -> None:
        # pandas code to remove an entry onto a data table
        pass

    # work in progress
    def editEntry(self, securityID: str, entryID: str, attribute: str, newData: str) -> None:
        # pandas code to edit an entry on a data table
        pass

    # work in progress
    def getEntryHistory(self) -> None:
        # return the data table
        pass
