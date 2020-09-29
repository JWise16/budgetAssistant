from userInfo.tableValue.tableValue import TableValue

"""
functions that work with savingsInfo.txt
"""


def createSavings(securityID, path) -> None:
    TableValue(securityID, path)


def createNewSavings(securityID, path) -> None:
    TableValue(securityID, path, 'savings', True, "Deosit_ammount", "Reason")


# work in progress
def addSavingsDeposit(date, amount, reason, tag=None) -> None:
    pass


# work in progress
def editSavingsDeposit(id, attribute, newData) -> None:
    pass


# work in progress
def removeSavingsDeposit(id) -> None:
    pass


# work in progress
def editSavingsHistory() -> None:
    pass


# work in progress
def viewSavingsHistory() -> None:
    pass
