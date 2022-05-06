# Menu1

co_name = "\niFeel"
print(co_name)

loading = "_" * 40
print(loading)

menu1 = """
Create new account = 1

Login = 2
"""
print(menu1)
print(loading)
menu1_choice = int(input("> "))

# Create new account. If menu1_choice == 1, it comes to these instructions.
# otherwise, it goes to the Login instructions.
# connect the userPersonal collection from iFeel db
new_user_instruct = "\n\nPlease enter your profile information\n"

print(new_user_instruct)
first_name = str(input("> First Name: "))
last_name = str(input("> Last Name: "))
e_mail = str(input("> Email: "))
username = str(input("> Username: "))
password = str(input("> Password: "))

save_profile = """
Save = 7

Cancel = 9  
"""
# if statement for if they choose Cancel here

print(loading)
print(save_profile)
print(loading)
save_profile_choice = int(input("> "))

# Login

login_instruct = "\n\nPlease enter your login credentials\n"
print(login_instruct)

existing_username = str(input("> Username: "))
existing_password = str(input("> Password: "))
# input fields for username and password variables. If credentials match existing users in DB, good.
# Otherwise, instruct to create new account.

# OR

# for the sake of being a beginner, as long as the data type is correct, that's all I care about
# for the MVP

# They will press enter after credentials.
login_success = "\nWelcome back\n\n\n\n"
print(login_success)


# Menu2
print(loading)
print(loading)
print(co_name)
print(loading)

menu2 = """
Add new mood = 1

View moods = 2

Edit profile = 3

Logout = 4

Delete account = 5
"""
print(menu2)
print(loading)
menu2_choice = int(input("> "))

# Add new mood
# connect the userMoods collection from iFeel db

greeting = """


Hello!

How do you feel today?
"""
print(greeting)
feelings = """
Happy = 1

Sad = 2

Fine = 3 
"""
print(feelings)
feeling_choice = int(input("> "))
send_off = "\nThank you\n"
print(send_off)
# insert username and feelings into userMoods collection

after_add_mood = """
Add another mood = 1

View moods = 2

Back = 9
"""
print(loading)
print(after_add_mood)
print(loading)
after_add_mood_choice = int(input("> "))

# View Moods
# run & and print a query from userMoods collection, using username field/variable.
# make the output pretty.

after_view_moods = """
Add new mood = 1

Back = 9
"""
print(loading)
print(after_view_moods)
print(loading)
after_view_moods_choice = int(input("> "))

# Edit Profile

edit_menu = """
What would you like to update?

First name = 1

Last name = 2

Email = 3

Username = 4

Password =5 
"""
print(loading)
print(edit_menu)
print(loading)
edit_menu_choice = int(input("> "))

# start an if loop, so that the query, input, update happens only for the field they specify.
# also make it ask if they want to edit anything else, yes or no. If yes, pull up the edit menu again,
# then it'll do the query, input, update for that one. When they say no, they don't want to edit
# anything else, then it goes to the after_edit screen.

# pattern: ask if they want to edit, query, input, update, repeat
# query & print first name
new_first_name = str(input("> New first name: "))
# update function

# query & print last name
new_last_name = str(input("> New last name: "))
# update function

# query & print email
new_email = str(input("> New Email: "))
# update function

# query & print username
new_username = str(input("> New username: "))
# update function

# query & print password
new_password = str(input("> New Password: "))

after_edit = """  
Changes saved

Back = 9
"""
print(loading)
print(after_edit)
print(loading)
after_edit_choice = int(input("> "))
# when they enter 9, it will take them back to menu2