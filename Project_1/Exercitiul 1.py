"""
Test bank account exercise
"""
expected_user: str = "Andrei"
expected_pwd: str = "123"
expected_sold: int = 100

# implementing the first test cases

user = input("please enter a user=")
assert user == expected_user
print(type(expected_sold))

pwd = input("please enter a password=")
assert pwd == expected_pwd

input("Please enter to login")
print(f"Login successful! your sold is={expected_sold} ")
print("Login successful! your sold is " + str(expected_sold))

cashback = int(input("Please enter the amount you want to retrive="))
print(f"You have= {expected_sold - cashback} Euro")

print(f"numarul de carectere din care este format numele este = {len(expected_user)} ")
b = len(expected_user) * "*"
print(f"numele dumneavoastra este = {b}")