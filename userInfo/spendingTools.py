from os import path
from typing import Optional
from userInfo.tableValue.tableValue import TableValue

"""
functions that work with savingsInfo.txt
"""


def loadSpendingHistory(securityID: str, file_path: str = '../userInfo/tableValue/tableData/purchaseInfo.csv') -> \
        Optional[TableValue]:
    """
    creates a TableValue object for a users purchase history from an exiting purchase data table file
    :param securityID: users ID
    :param file_path: path to the purchase data table file
    :return: TableValue object for purchase history or None if a data file is not found
    """
    if path.exists(file_path):
        return TableValue(securityID, file_path)
    else:
        print('Data File Does not exist for the purchase information... Please call createNewPurchaseHistory()')
        return None


def createNewSpendingHistory(securityID: str, file_path: str = '../userInfo/tableValue/tableData/purchaseInfo.csv') -> \
        Optional[TableValue]:
    """
    creates a TableValue object for a users purchase history and creates a new
    purchase data table file
    :param securityID: users ID
    :param file_path: path to the purchase data table file
    :return: TableValue object for a users purchase history or call createPurchaseHistory() if a data table file
     is already found
    """
    if not path.exists(file_path):
        return TableValue(securityID, file_path, "Purchase", True, "Transaction_amount", "Reason")
    else:
        print('Data file already exists for the purchase information... calling createPurchaseHistory())')
        loadSpendingHistory(securityID, file_path)


def addTransaction(table_value: TableValue, securityID: str, date: str, amount: float, reason: str,
                   tag: str = "N/A") -> None:
    """
    adds a transaction into the users purchase history
    (a transaction is a... date, transaction amount, transaction reason, and a tag)
    :param table_value: TableValue object where the purchase information is stored
    :param securityID: users security ID
    :param date: the date the transaction occured
    :param amount: amount the transaction was
    :param reason: reason the transaction occured
    :param tag: tags that group transactions together (default "N/A")
    :return: None
    """
    table_value._addEntry(securityID, date, amount, reason, tag)


def editTransaction(table_value: TableValue, securityID: str, entry_index: int, column_name: str,
                    new_data) -> None:
    """
    edits a single entry in a transaction
    :param table_value: TableValue object that stores the users purchase information
    :param securityID: users security ID
    :param entry_index: index of the entry to be edited
    :param column_name: which column is to be edited
    :param new_data: new data to be inserted into the entry
    :return: None
    """
    table_value._editEntry(securityID, entry_index, column_name, new_data)


def removeTransaction(table_value: TableValue, securityID: str, entry_index: int) -> None:
    """
    removes a transaction
    :param table_value: TableValue object that stores the users purchase information
    :param securityID: the users security ID
    :param entry_index: the index of the savings deposit to be removed
    :return: None
    """
    table_value._removeEntry(securityID, entry_index)


def getSpendingData(table_value: TableValue, securityID: str) -> dict:
    """
    returns the data table which is a dictionary with column names as keys and lists that represent data entries
    as values
    :param table_value: TableValue object which contains the purchase data
    :param securityID: users security ID
    :return: data table (Type dict)
    """
    return dict(table_value._data(securityID))

def printSpendingData(spending: TableValue, securityID: str) -> None:
    """
    prints the spending data into the console
    :param spending: TableValue object that holds that savings data
    :param securityID: users security ID
    :return: None
    """
    print("Savings")
    print("Date    Transaction_amount    Reason    Tag")
    data = getSpendingData(spending, securityID)
    for i in range(0, len(data['Date'])):
        print(data['Date'][i], data['Transaction_amount'][i], data['Reason'][i], data["Tag"][i])
