from userInfo.singleValue.singleValue import SingleValue
import csv


class TableValue(SingleValue):

    def __init__(self, securityID: str, path: str, storage: str = None, new_data_table=False, col_one_name='',
                 col_two_name=''):
        """
        Constructor for the TableValue class. Makes a new data table file if needed, and always calls the constructor of
        SingleValue where self._info is made.
        :param securityID: users securityID
        :param path: path to data file
        :param storage: type of data the TableValue will hold
        :param new_data_table: True/False for if a new data table file needs to be made
        :param col_one_name: (use if new_data_table == True) First column name for variable data
        :param col_two_name: (use if new_data_table == True) Second column name for variable data
        """
        if new_data_table:
            self._newDataTable(securityID, path, storage, col_one_name, col_two_name)
        super().__init__(securityID, path)
        self._loadDataTable(path)

    def _addEntry(self, securityID: str, date: str, val_one: object, val_two: object, tag: str = "N/A", ) -> None:
        """
        Adds an entry (a date, 2 variable data, and a tag) onto the data table
        :param securityID: users security ID
        :param date: date of the entry
        :param val_one: col_one_name value
        :param val_two: col_two_name value
        :param tag: tag to group entry with other entries
        :return: None
        """
        col_names = self._info['col_names']
        self.idCheck(securityID)
        # add date
        self._info['data'][col_names[0]].append(date)
        # add first stored value
        self._info['data'][col_names[1]].append(val_one)
        # add second stored value
        self._info['data'][col_names[2]].append(val_two)
        # add tag
        self._info['data'][col_names[3]].append(tag)

    def _removeEntry(self, securityID: str, entryIndex: int) -> None:
        """
        removes an entry from the data table based off of the index of the entry
        :param securityID: users security ID
        :param entryIndex: index of the entry to be removed
        :return: None
        """
        self.idCheck(securityID)
        col_names = self._info['data'].keys()
        for column in col_names:
            del self._info['data'][column][entryIndex]

    def _editEntry(self, securityID: str, entryIndex: int, column: str, newData: object) -> None:
        """
        change a entry on the table based off of column and index
        :param securityID: users security ID
        :param entryIndex: index of the entry to be edited
        :param column: column to be edited
        :param newData: new data to be inserted into the data table
        :return: None
        """
        self.idCheck(securityID)
        self._info['data'][column][entryIndex] = newData

    def _newDataTable(self, securityID: str, path: str, storage_type: str, column_name_one: str,
                      column_name_two: str) -> None:
        """
        creates a new data table file
        format:
        securityID
        storage_type
        data...
        :param securityID: users securityID
        :param path: new data files path
        :param storage_type: type of data the table will be storing
        :param column_name_one: first variable data column
        :param column_name_two: second variable data column
        :return:
        """
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([securityID])
            writer.writerow([storage_type])
            writer.writerow(['Date', column_name_one, column_name_two, 'Tag'])
            f.close()

    def _writeDataTable(self, securityID: str, path: str, type: str, column_name_one: str,
                        column_name_two: str) -> None:
        """
        writes a data table to a file, can be used to "update" a existing data table file
        :param securityID: users security ID
        :param path: path to the data table file
        :param type: type of data that will be stored in the table
        :param column_name_one: name of the first variable data column
        :param column_name_two: name of the second variable data column
        :return: none
        """
        col_names = self._info['col_names']
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([securityID])
            writer.writerow([type])
            writer.writerow(col_names)

            dates = self._info['data'][col_names[0]]
            col_one = self._info['data'][col_names[1]]
            col_two = self._info['data'][col_names[2]]
            tags = self._info['data'][col_names[3]]

            num_entries = len(self._info['data'][col_names[0]])
            for index in range(0, num_entries):
                writer.writerow([dates[index], col_one[index], col_two[index], tags[index]])
            f.close()

    def _loadDataTable(self, path) -> None:
        """
        loads a data table into self._info from a data table file
        :param path: file path to the data table
        :return: None
        """
        with open(path, 'r') as f:
            reader = csv.reader(f)
            self._info['id'] = next(reader)[0]
            self._info['type'] = next(reader)[0]
            self._info['col_names'] = next(reader)
            col_names = self._info['col_names']
            if len(self._info["col_names"]) != 4:
                print('id', self._info['id'])
                print('type', self._info['type'])
                print('col_names', col_names)
                raise ValueError("not enough columns in col_names")
            data = {col_names[0]: [], col_names[1]: [], col_names[2]: [], col_names[3]: []}
            for line in reader:
                for index in range(0, len(col_names) - 1):
                    if line[index] is not None:
                        data[col_names[index]].append(line[index])
            self._info['data'] = data
