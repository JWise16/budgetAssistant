from userInfo import spendingTools, savingsTools, workTools
from os import remove


def trackSpend(info: dict) -> None:
    running = True
    while running:
        print('Which spending feature would you like to use?')
        option = int(input(
            "View transaction history (1)\nAdd a transaction (2)\nEdit a transaction (3)\nRemove a transaction (4)\n"))
        if option == 1:
            print("Bringing up the transaction history...")
            spendingTools.getSpendingData(info['Purchase'], info['ID'])
        elif option == 2:
            print("Adding a transaction...")
            date = input("Date of transaction: ")
            amount = float(input("Transaction amount(number... ex: 34.42): "))
            reason = input("Reason for transaction: ")
            tag = input("Tag to group transactions together: ")
            spendingTools.addTransaction(info['Purchase'], info['ID'], date, amount, reason, tag)
        elif option == 3:
            print("Editing a transaction...")
            entry_index = int(input("Entry index(int): "))
            column_name = input("Column name: ")
            new_data = input("New data: ")
            spendingTools.editTransaction(info['Purchase'], info['ID'], entry_index, column_name, new_data)
        elif option == 4:
            print("Removing a transaction")
            entry_index = int(input("Entry index: "))
            spendingTools.removeTransaction(info['Purchase'], info['ID'], entry_index)
        else:
            print("Feature not found, please try again")
        exit_loop = True
        while exit_loop:
            cont = input("Would you like to continue looking at your spending data? (y/n)")
            if cont == 'y':
                exit_loop = False
            elif cont == 'n':
                exit_loop = False
                running = False
                print("Returning to main program")
            else:
                print("Input not recognized, please try again")


def trackWork(info: dict) -> None:
    running = True
    while running:
        print('Which work feature would you like to use?')
        option = int(input(
            "View work history (1)\nAdd a shift (2)\nEdit a shift (3)\nRemove a shift (4)\n"))
        if option == 1:
            print("Bringing up the work history...")
            workTools.getWorkData(info['Work'], info['ID'])
        elif option == 2:
            print("Adding a shift...")
            date = input("Date of shift: ")
            hours = float(input("Hours worked(number... ex: 6.3): "))
            dol_per_hour = float(input("Dollars per hour(number... ex: 12.25): "))
            tag = input("Tag to group shifts together: ")
            workTools.addShift(info['Purchase'], info['ID'], date, hours, dol_per_hour, tag)
        elif option == 3:
            print("Editing a shift...")
            entry_index = int(input("Entry index(int): "))
            column_name = input("Column name: ")
            new_data = input("New data: ")
            workTools.editShift(info['Work'], info['ID'], entry_index, column_name, new_data)
        elif option == 4:
            print("Removing a shift")
            entry_index = int(input("Entry index: "))
            spendingTools.removeTransaction(info['Work'], info['ID'], entry_index)
        else:
            print("Feature not found, please try again")
        exit_loop = True
        while exit_loop:
            cont = input("Would you like to continue looking at your work data? (y/n)")
            if cont == 'y':
                exit_loop = False
            elif cont == 'n':
                exit_loop = False
                running = False
                print("Returning to main directory")
            else:
                print("Input not recognized, please try again")


def trackSave(info: dict) -> None:
    running = True
    while running:
        print('Which savings feature would you like to use?')
        option = int(input(
            "View savings history (1)\nAdd a deposit (2)\nEdit a deposit (3)\nRemove a deposit (4)\n"))
        if option == 1:
            print("Bringing up the savings history...")
            savingsTools.getSavingsData(info['Savings'], info['ID'])
        elif option == 2:
            print("Adding a deposit...")
            date = input("Date of deposit: ")
            amount = float(input("Amount deposited(number... ex: 120.23): "))
            reason = input("Reason for deposit: ")
            tag = input("Tag to group deposits together: ")
            savingsTools.addSavingsDeposit(info['Savings'], info['ID'], date, amount, reason, tag)
        elif option == 3:
            print("Editing a deposit...")
            entry_index = int(input("Entry index(int): "))
            column_name = input("Column name: ")
            new_data = input("New data: ")
            savingsTools.editSavingsDeposit(info['Savings'], info['ID'], entry_index, column_name, new_data)
        elif option == 4:
            print("Removing a deposit")
            entry_index = int(input("Entry index: "))
            savingsTools.removeSavingsDeposit(info['Savings'], info['ID'], entry_index)
        else:
            print("Feature not found, please try again")
        exit_loop = True
        while exit_loop:
            cont = input("Would you like to continue looking at your savings data? (y/n)")
            if cont == 'y':
                exit_loop = False
            elif cont == 'n':
                exit_loop = False
                running = False
                print("Returning to main directory")
            else:
                print("Input not recognized, please try again")


def writeInfo(user_info: dict) -> None:
    user_info['ID']._write

def removeInfoData() -> None:
    remove("../userInfo/singleValue/infoData/emailInfo.csv")
    remove("../userInfo/singleValue/infoData/passwordInfo.csv")
    remove("../userInfo/singleValue/infoData/securityInfo.csv")
    remove("../userInfo/singleValue/infoData/usernameInfo.csv")


def removeTableData() -> None:
    remove("../userInfo/tableValue/tableData/purchaseInfo.csv")
    remove("../userInfo/tableValue/tableData/savingsInfo.csv")
    remove("../userInfo/tableValue/tableData/workInfo.csv")
