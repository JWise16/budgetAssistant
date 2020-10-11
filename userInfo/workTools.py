from os import path
from typing import Optional
from userInfo.tableValue.tableValue import TableValue

"""
functions that work with savingsInfo.txt
"""


def loadWorkLog(securityID: str, file_path: str = '../userInfo/tableValue/tableData/workInfo.csv') -> Optional[
    TableValue]:
    """
    creates a TableValue object for a users work log from an exiting work log data table file
    :param securityID: users ID
    :param file_path: path to the work log data table file
    :return: TableValue object for a work log or None if a data file is not found
    """
    if path.exists(file_path):
        return TableValue(securityID, file_path)
    else:
        print('Data File Does not exist for the work log... Please call createNewWorkLog()')
        return None


def createNewWorkLog(securityID: str, file_path: str = '../userInfo/tableValue/tableData/workInfo.csv') -> Optional[
    TableValue]:
    """
    creates a TableValue object for a users work log and creates a new
    work log data table file
    :param securityID: users ID
    :param file_path: path to the work log data table file
    :return: TableValue object for a users work log or call createWorkLog() if a data table file is already found
    """
    if not path.exists(file_path):
        return TableValue(securityID, file_path, "Work", True, "Hours", "Dollars_per_hour")
    else:
        print('Data file already exists for the work log... calling createWorkLog()')
        loadWorkLog(securityID, file_path)


def addShift(table_value: TableValue, securityID: str, date: str, hours: float, dollars_per_hour: float,
             tag: str = "N/A") -> None:
    """
    adds a shift into the users work log
    (a shift is a... date, hours worked, dollars per hour, and a tag(optional, groups deposits together))
    :param table_value: TableValue object where the savings information is stored
    :param securityID: users security ID
    :param date: the date the savings deposit occured
    :param hours: amount added into savings
    :param dollars_per_hour: reason the amount was added into savings
    :param tag: tags that group savings deposits together (default "N/A")
    :return: None
    """
    table_value._addEntry(securityID, date, hours, dollars_per_hour, tag)


def editShift(table_value: TableValue, securityID: str, entry_index: int, column_name: str,
              new_data: object) -> None:
    """
    edits a single entry in a shift
    :param table_value: TableValue object that stores the users savings information
    :param securityID: users security ID
    :param entry_index: index of the entry to be edited
    :param column_name: which column is to be edited
    :param new_data: new data to be inserted into the entry
    :return: None
    """
    table_value._editEntry(securityID, entry_index, column_name, new_data)


def removeShift(table_value: TableValue, securityID: str, entry_index: int) -> None:
    """
    removes a savings deposit
    :param table_value: TableValue object that stores the users savings information
    :param securityID: the users security ID
    :param entry_index: the index of the savings deposit to be removed
    :return: None
    """
    table_value._removeEntry(securityID, entry_index)


def getWorkData(table_value: TableValue, securityID: str) -> dict:
    """
    returns the data table which is a dictionary with column names as keys and lists that represent data entries
    as values
    :param table_value: TableValue object which contains the work data
    :param securityID: users security ID
    :return: data table (Type dict)
    """
    return dict(table_value._data(securityID))
