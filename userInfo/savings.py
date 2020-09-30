from os import path
from typing import Optional
from userInfo.tableValue.tableValue import TableValue

"""
functions that work with savingsInfo.txt
"""


def createSavings(securityID: str, file_path: str = 'userInfo/tableValue/tableData/savingsInfo.csv') -> Optional[
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


def createNewSavings(securityID: str, file_path: str = 'userInfo/tableValue/tableData/savingsInfo.txt') -> Optional[
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
        createSavings(securityID, file_path)


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
    table_value.addEntry(securityID, date, amount, reason, tag)


def editSavingsDeposit(table_value: TableValue, securityID: str, entry_index: int, column_name: str,
                       new_data: int) -> None:
    """
    edits a single entry in a savings deposit
    :param table_value: TableValue object that stores the users savings information
    :param securityID: users security ID
    :param entry_index: index of the entry to be edited
    :param column_name: which column is to be edited
    :param new_data: new data to be inserted into the entry
    :return: None
    """
    table_value.editEntry(securityID, entry_index, column_name, new_data)


def removeSavingsDeposit(table_value: TableValue, securityID: str, entry_index: int) -> None:
    """
    removes a savings deposit
    :param table_value: TableValue object that stores the users savings information
    :param securityID: the users security ID
    :param entry_index: the index of the savings deposit to be removed
    :return: None
    """
    table_value.removeEntry(securityID, entry_index)


# work in progress
def editSavingsHistory() -> None:
    pass


# work in progress
def viewSavingsHistory() -> None:
    pass
