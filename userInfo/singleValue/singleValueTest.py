from userInfo.singleValue.singleValue import SingleValue

print("Testing construction without an existing data file...\n")
s = SingleValue("8416826", 'userInfo/singleValue/infoData/testSingleValue.csv', 'type', 'data')
first_path = s._path("8416826")
first_type = s._type("8416826")
first_data = s._data("8416826")

s._changeInfo("8416826", 'data', 'Jonathanwise16@gmail.com')
first_data_two = s._data("8416826")
print("All methods tested with new data file construction!\n\n")

print("Testing construction from an existing data file...\n")
v = SingleValue("8416826", 'userInfo/singleValue/infoData/testSingleValue.csv')
second_path = v._path("8416826")
second_type = v._type("8416826")
second_data = v._data("8416826")

v._changeInfo("8416826", 'data', 'Jonathanwise16@gmail.com')
second_data_two = v._data("8416826")

v._removeDataFile("8416826")
print("All methods tested with existing data file construction!\n\n")
print("Both tests have the same...")
print("Path:", first_path == second_path)
print("Type:", first_type == second_type)
print("Data:", first_data == second_data)
print("Changed data:", first_data_two == second_data_two)
