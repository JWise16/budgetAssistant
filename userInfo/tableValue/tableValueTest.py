from userInfo.tableValue.tableValue import TableValue

# 8416826

print("Testing construction without an existing data table file")
t = TableValue("8416826", "userInfo/tableValue/tableData/temporaryFile.csv", "TableValueStorage", True, "Column_one",
               "Column_two")

t._addEntry("8416826", "06/16/2002", "first data0", "second data0", ['Date', 'Column_one', 'Column_two', 'Tag'],
            "ThisTag")
t._addEntry("8416826", "08/16/2002", "first data1", "second data1", ['Date', 'Column_one', 'Column_two', 'Tag'],
            "ThisTag1")
t._addEntry("8416826", "09/16/2002", "first data2", "second data2", ['Date', 'Column_one', 'Column_two', 'Tag'],
            "ThisTag")
t._addEntry("8416826", "09/16/2002", "first data3", "second data3", ['Date', 'Column_one', 'Column_two', 'Tag'],
            "ThisTag1")

input("Verify self._info['data'] data table looks all good. Press 'enter' to continue")
print("removing the third entry and editing the first column variable data in the first row")
t._removeEntry("8416826", 2)
t._editEntry("8416826", 0, "Column_one", "edited data0")

input("Verify self._info['data'] data table looks all good. Press 'enter' to continue")
input("Look at the data table in 'temporaryFile.csv'\nPress enter to load the new data table into 'temporaryFile.csv'")
t.writeDataTable("8416826", 'userInfo/tableValue/tableData/temporaryFile.csv', 'TableValueStorage', 'Column_one',
                 'Column_two')

input("Verify all TableValue data is correct\nPress 'enter' to continue")
print("Testing construction from the existing data table file")
t_2 = TableValue("8416826", "userInfo/tableValue/tableData/temporaryFile.csv")

print("Calling most SingleValue methods and checking for equality among the two objects")
first_path = t._path("8416826")
first_type = t._type("8416826")
first_data = t._data("8416826")

second_path = t_2._path("8416826")
second_type = t_2._type("8416826")
second_data = t_2._data("8416826")

print("Both tests have the same...")
print("Path:", first_path == second_path)
print("Type:", first_type == second_type)
print("Data:", first_data == second_data)

input("Press 'enter' to remove 'temporaryFile.csv' and end the test")

# t._removeDataFile("8416826")
