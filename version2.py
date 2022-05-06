# Menu1
# connect the userPersonal collection from iFeel db

co_name = "\niFeel"
loading = "_" * 40
menu1 = """
Create new account = 1

Login = 2
"""

# Create new account

new_user_instruct = "\n\nPlease enter your profile information\n"

# Login
login_instruct = "\n\nPlease enter your login credentials\n"
login_success = "\nWelcome back\n\n\n\n"

# Menu2
menu2 = """
Add new mood = 1

View moods = 2

Edit profile = 3

Logout = 4

Delete account = 5
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
send_off = "\nThank you\n"

# View Moods
# run & and print a query from userMoods collection, using username field/variable.
# make the output pretty.

after_view_moods = "\nBack = 9"

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

Password =5 


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
print(menu1)
print(loading)
menu1_choice = int(input("> "))

if menu1_choice == 1:
    print(new_user_instruct)
    first_name = str(input("> First Name: "))
    last_name = str(input("> Last Name: "))
    e_mail = str(input("> Email: "))
    username = str(input("> Username: "))
    password = str(input("> Password: "))
elif menu1_choice == 2:
    print(login_instruct)
    existing_username = str(input("> Username: "))
    existing_password = str(input("> Password: "))
    print(login_success)
print(loading)
print(loading)
print(co_name)
print(loading)
print(menu2)
print(loading)
menu2_choice = int(input("> "))
if menu2_choice == 1:
    print(greeting)
    print(feelings)
    feeling_choice = int(input("> "))
    if feeling_choice == 1:
        print("Gotcha. I've recorded your mood for you.")  # return to menu2 after this message
    elif feeling_choice == 2:
        print("I understand. I've recorded your mood for you.")  # return to menu2 after this message
    elif feeling_choice == 3:
        print("I hear you. I've recorded your mood for you.")  # return to menu2 after this message
    print(print(send_off))
elif menu2_choice == 2:
    print(loading)
    print(after_view_moods)
    print(loading)
    after_view_moods_choice = int(input("> "))
elif menu2_choice == 3:
    print(loading)
    print(edit_menu)
    print(loading)
    edit_menu_choice = int(input("> "))
    if edit_menu_choice == 1:
        new_first_name = str(input("> New first name: "))  # decide where it goes they update
    elif edit_menu_choice == 2:
        new_last_name = str(input("> New last name: "))  # decide where it goes after they update
    elif edit_menu_choice == 3:
        new_email = str(input("> New Email: "))  # decide where it goes after they update
    elif edit_menu_choice == 4:
        new_username = str(input("> New username: "))  # decide where it goes after they update
    elif edit_menu_choice == 5:
        new_password = str(input("> New Password: "))  # decide where it goes after they update
    elif edit_menu_choice == 9:
        print(loading)
        print(loading)
        print(co_name)
        print(loading)
        print(menu2)
        print(loading)
        menu2_choice = int(input("> "))
elif menu2_choice == 4:
    print(logout_msg)
    print(loading)
    print(logout_menu)
    print(loading)
    logout_menu_choice = int(input("> "))  # if logout_menu_choice == 1: return to menu1
elif menu2_choice == 5:
    print(delete_msg)
    delete_menu_choice = (input("> "))
    if delete_menu_choice == 1:
        print(confirm_delete)  # return to menu1 after deletion
    elif delete_menu_choice == 2:
        print(loading)
        print(loading)
        print(co_name)
        print(loading)
        print(menu2)
        print(loading)
        menu2_choice = int(input("> "))
