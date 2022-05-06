import pymongo

mongo = pymongo.MongoClient('mongodb://localhost:27017')
db = mongo['iFeel']
collection1 = db['userMoods']
collection2 = db['userPersonal']

# Menu1
# connect the userPersonal collection from iFeel db

co_name = "\niFeel"
loading = "_" * 40

# Create new account

new_user_instruct = """

Welcome to iFeel

Please create an account to get started
"""

# Menu2
menu2 = """
Add new mood = 1

Profile = 2

Logout = 3

Delete account = 4
"""

# Add new mood
# # insert username and feelings into userMoods collection

greeting = """
Hello!

How do you feel today?
"""
feelings = """
Happy = 1

Sad = 2

Fine = 3 

"""

# Edit Profile
# start an if loop, so that the query, input, update happens only for the field they specify.
# also make it ask if they want to edit anything else, yes or no. If yes, pull up the edit menu again,
# then it'll do the query, input, update for that one. When they say no, they don't want to edit
# anything else, then it goes to the after_edit screen.

# pattern: ask if they want to edit, query, input, update, repeat

edit_menu = """
What would you like to update?

First name = 1

Last name = 2

Email = 3

Username = 4

Password = 5 


Back = 9
"""

# Logout

logout_msg = "Thank you - talk you to next time!"

logout_menu = """
Login = 1

Exit =2 
"""

# Delete account
delete_msg = "Are you sure you want to delete your account?"
delete_menu = """
Delete = 1

Cancel = 2
"""
confirm_delete = """
Sorry to see you go...

Your account has been deleted
"""

# ____________________________________________________________________________
# MAIN PROGRAM
# ____________________________________________________________________________

print(co_name)
print(loading)
print(new_user_instruct)
first_name = str(input("> First Name: "))
last_name = str(input("> Last Name: "))
e_mail = str(input("> Email: "))
username = str(input("> Username: "))
password = str(input("> Password: "))
print(loading)
print(loading)
print(loading)
print(menu2)
menu2_choice = int(input("> "))
while menu2_choice == 1:
    print(loading)
    print(greeting)
    print(feelings)
    feeling_choice = int(input("> "))
    if feeling_choice == 1:
        print("\nGotcha. I've recorded your mood for you.\n\n")
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
    elif feeling_choice == 2:
        print("\nI understand. I've recorded your mood for you.\n\n")
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
    elif feeling_choice == 3:
        print("\nI hear you. I've recorded your mood for you.\n\n")
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
while menu2_choice == 2:
    print(loading)
    print(edit_menu)
    edit_menu_choice = int(input("> "))
    if edit_menu_choice == 1:
        new_first_name = str(input("> New first name: "))
        print("\nSaved!\n")
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
    elif edit_menu_choice == 2:
        new_last_name = str(input("> New last name: "))
        print("\nSaved!\n")
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
    elif edit_menu_choice == 3:
        new_email = str(input("> New Email: "))
        print("\nSaved!\n")
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
    elif edit_menu_choice == 4:
        new_username = str(input("> New username: "))
        print("\nSaved!\n")
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
    elif edit_menu_choice == 5:
        new_password = str(input("> New Password: "))
        print("\nSaved!\n")
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
    elif edit_menu_choice == 9:
        print("\nSaved!\n")
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
if menu2_choice == 3:
    print(logout_msg)
while menu2_choice == 4:
    print(delete_msg)
    print(delete_menu)
    delete_menu_choice = int((input("> ")))
    if delete_menu_choice == 1:
        print(confirm_delete)
        break
    elif delete_menu_choice == 2:
        print(loading)
        print(loading)
        print(loading)
        print(menu2)
        menu2_choice = int(input("> "))
