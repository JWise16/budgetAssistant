from os import path
from typing import Optional
from userInfo.tableValue.tableValue import TableValue

"""
functions that work with savingsInfo.txt
"""


def loadSavings(securityID: str, file_path: str = '../userInfo/tableValue/tableData/savingsInfo.csv') -> Optional[
    TableValue]:
    """
    creates a TableValue object for a users savings from an exiting savings data table file
    :param securityID: users ID
    :param file_path: path to the savings data table file
    :return: TableValue object for savings or None if a data file is not found
    """
    if path.exists(file_path):
        return TableValue(securityID, file_path)
    else:
        print('Data File Does not exist for savings... Please call createNewSavings()')
        return None


def createNewSavings(securityID: str, file_path: str = '../userInfo/tableValue/tableData/savingsInfo.csv') -> Optional[
    TableValue]:
    """
    creates a TableValue object for a users savings and creates a new
    savings data table file
    :param securityID: users ID
    :param file_path: path to the savings data table file
    :return: TableValue object for a users savings or call createSavings() if a data table file is already found
    """
    if not path.exists(file_path):
        return TableValue(securityID, file_path, "Savings", True, "Deposit_amount", "Reason")
    else:
        print('Data file already exists for savings... calling createSavings()')
        loadSavings(securityID, file_path)


def addSavingsDeposit(table_value: TableValue, securityID: str, date: str, amount: float, reason: str,
                      tag: str = "N/A") -> None:
    """
    adds a savings deposit into the users savings history
    (a savings deposit is a... date, deposit amount, deposit reason, and a tag(optional, groups deposits together))
    :param table_value: TableValue object where the savings information is stored
    :param securityID: users security ID
    :param date: the date the savings deposit occured
    :param amount: amount added into savings
    :param reason: reason the amount was added into savings
    :param tag: tags that group savings deposits together (default "N/A")
    :return: None
    """
    table_value._addEntry(securityID, date, amount, reason, tag)


def editSavingsDeposit(table_value: TableValue, securityID: str, entry_index: int, column_name: str,
                       new_data) -> None:
    """
    edits a single entry in a savings deposit
    :param table_value: TableValue object that stores the users savings information
    :param securityID: users security ID
    :param entry_index: index of the entry to be edited
    :param column_name: which column is to be edited
    :param new_data: new data to be inserted into the entry
    :return: None
    """
    table_value._editEntry(securityID, entry_index, column_name, new_data)


def removeSavingsDeposit(table_value: TableValue, securityID: str, entry_index: int) -> None:
    """
    removes a savings deposit
    :param table_value: TableValue object that stores the users savings information
    :param securityID: the users security ID
    :param entry_index: the index of the savings deposit to be removed
    :return: None
    """
    table_value._removeEntry(securityID, entry_index)


def getSavingsData(savings: TableValue, securityID: str) -> dict:
    """
    returns the data table which is a dictionary with column names as keys and lists that represent data entries
    as values
    :param table_value: TableValue object which contains the savings data
    :param securityID: users security ID
    :return: data table (Type dict)
    """
    return dict(savings._data(securityID))


def printSavingsData(savings: TableValue, securityID: str) -> None:
    """
    prints the savings data into the console
    :param savings: TableValue object that holds that savings data
    :param securityID: users security ID
    :return: None
    """
    print("Savings")
    print("Date    Deposit_amount    Reason    Tag")
    data = getSavingsData(savings, securityID)
    for i in range(0, len(data['Date'])):
        print(data['Date'][i], data['Deposit_amount'][i], data['Reason'][i], data["Tag"][i])
