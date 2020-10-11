from userInfo import emailTools, passwordTools, spendingTools, savingsTools, usernameTools, workTools

# TODO: Fix construction from an existing file (the problem may be that the objects are not writing to the new files,
#  not that the objects are reading the files incorrectly)

# TODO: remove large package from github repository


print("Testing email construction and methods...")
user_email = emailTools.createNewEmail("8416826", "jonathanwise16@gmail.com",
                                       "userInfo/singleValue/infoData/emailTest.csv")
print("First email:", emailTools.getEmail("8416826", user_email))
emailTools.changeEmail("8416826", "jon13086@gmail.com", user_email)
print("Second email:", emailTools.getEmail("8416826", user_email), '\n')

print("Testing password construction and methods...")
user_password = passwordTools.createNewPassword("8416826", "JonnysPassword",
                                                "userInfo/singleValue/infoData/passwordTest.csv")
print("First password:", passwordTools.getPassword("8416826", user_password))
passwordTools.changePassword("8416826", "JonnysNewPassword", user_password)
print("Second password:", passwordTools.getPassword("8416826", user_password), '\n')

print("Testing username construction and methods...")
user_username = usernameTools.createNewUsername("8416826", "JonathanWise",
                                                "userInfo/singleValue/infoData/usernameTest.csv")
print("First username:", usernameTools.getUsername("8416826", user_username))
usernameTools.changeUsername("8416826", "JonathanWise2.0", user_username)
print("Second username:", usernameTools.getUsername("8416826", user_username), '\n')

print("Removing email, password, and username data files\n\n")
user_email._removeDataFile("8416826")
user_password._removeDataFile("8416826")
user_username._removeDataFile("8416826")

print("Testing purchase construction and methods...")
user_purchase = spendingTools.createNewSpendingHistory("8416826", 'userInfo/tableValue/tableData/purchaseTest.csv')
spendingTools.addTransaction(user_purchase, "8416826", "9/30/20", 20, "gas station", "gas")
data_tree = spendingTools.getSpendingData(user_purchase, "8416826")
print("Data entry:", data_tree['Date'][0], data_tree['Transaction_amount'][0], data_tree['Reason'][0],
      data_tree['Tag'][0])
spendingTools.editTransaction(user_purchase, "8416826", 0, "Transaction_amount", 30)
data_tree = spendingTools.getSpendingData(user_purchase, "8416826")
print("Data entry edited:", data_tree['Date'][0], data_tree['Transaction_amount'][0], data_tree['Reason'][0],
      data_tree['Tag'][0])
spendingTools.removeTransaction(user_purchase, "8416826", 0)

print("Testing savings construction and methods...")
user_savings = savingsTools.createNewSavings("8416826", 'userInfo/tableValue/tableData/savingsTest.csv')
savingsTools.addSavingsDeposit(user_savings, "8416826", "9/30/20", 300, "Monthly savings deposit", "G")
data_tree = savingsTools.getSavingsData(user_savings, "8416826")
print("Data entry:", data_tree['Date'][0], data_tree['Deposit_amount'][0], data_tree['Reason'][0], data_tree['Tag'][0])
savingsTools.editSavingsDeposit(user_savings, "8416826", 0, "Deposit_amount", 299)
data_tree = savingsTools.getSavingsData(user_savings, "8416826")
print("Data entry edited:", data_tree['Date'][0], data_tree['Deposit_amount'][0], data_tree['Reason'][0],
      data_tree['Tag'][0])
savingsTools.removeSavingsDeposit(user_savings, "8416826", 0)

print("Testing work construction and methods...")
user_work = workTools.createNewWorkLog("8416826", 'userInfo/tableValue/tableData/workTest.csv')
workTools.addShift(user_work, "8416826", "9/30/20", 8, 20, "P")
data_tree = workTools.getWorkData(user_work, "8416826")
print("Data entry:", data_tree['Date'][0], data_tree['Hours'][0], data_tree['Dollars_per_hour'][0], data_tree['Tag'][0])
workTools.editShift(user_work, "8416826", 0, "Hours", 10)
data_tree = workTools.getWorkData(user_work, "8416826")
print("Data entry edited:", data_tree['Date'][0], data_tree['Hours'][0], data_tree['Dollars_per_hour'][0],
      data_tree['Tag'][0])
workTools.removeShift(user_work, "8416826", 0)

user_purchase._removeDataFile("8416826")
user_savings._removeDataFile("8416826")
user_work._removeDataFile("8416826")
