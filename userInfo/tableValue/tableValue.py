from userInfo.singleValue.singleValue import SingleValue
import csv


class TableValue(SingleValue):

    def __init__(self, securityID: str, path: str, storage: str = None, new_data_table=False, col_one_name='',
                 col_two_name=''):
        if new_data_table:
            self.newDataTable(securityID, path, storage, col_one_name, col_two_name)
        super().__init__(securityID, path, storage, "tableData")

    def addEntry(self, securityID: str, date: str, val_one: str, val_two: str, tag: str = "N/A") -> None:
        self.idCheck(securityID)
        col_names = self._info['data'].keys()

        # add date
        self._info['data'][col_names[0]].append(date)
        # add first stored value
        self._info['data'][col_names[1]].append(val_one)
        # add second stored value
        self._info['data'][col_names[2]].append(val_two)
        # add tag
        self._info['data'][col_names[3]].append(tag)

    def removeEntry(self, securityID: str, entryIndex: str) -> None:
        self.idCheck(securityID)
        col_names = self._info['data'].keys()
        for item in col_names:
            del self._info['data'][item][entryIndex]

    def editEntry(self, securityID: str, entryIndex: str, attribute: str, newData: object) -> None:
        self.idCheck(securityID)
        self._info['data'][attribute][entryIndex] = newData

    # TODO: make method that can create and write to a file
    def newDataTable(self, securityID: str, path: str, type: str, name_one: str, name_two: str):
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([securityID])
            writer.writerow([type])
            writer.writerow(['Date', name_one, name_two, 'Tag'])
            f.close()

    def writeDataTable(self, securityID: str, path: str, type: str, name_one: str, name_two: str):
        col_names = self._info['data'].keys()
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([securityID])
            writer.writerow([type])
            writer.writerow(['Date', name_one, name_two, 'Tag'])
            for index in range(0, len(self._info['data'][col_names[0]] - 1)):
                dates = self._info['data'][col_names[0]]
                col_one = self._info['data'][col_names[1]]
                col_two = self._info['data'][col_names[2]]
                tags = self._info['data'][col_names[3]]
                writer.writerow([dates[index], col_one[index], col_two[index]])
            f.close()

    def loadDataTable(self, path) -> None:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            self._info['id'] = next(reader)
            self._info['type'] = next(reader)
            col_names = next(reader)
            data = {col_names[0]: [], col_names[1]: [], col_names[2]: [], col_names[3]: []}
            for line in reader:
                for index in range(0, col_names - 1):
                    data[col_names[index]].append(line[index])
            self._info['data'] = data
