import pymongo
mongo = pymongo.MongoClient('mongodb://localhost:27017')
db = mongo['iFeel']
collection1 = db['userMoods']
collection2 = db['userGoals']

co_name = "\niFeel"
loading = "_" * 40
user = "Morgan"
# Menu2
menu2 = """
Add Mood = 1

Set Goal = 2

Exit = 3
"""

# Add new mood

mood_greeting = "\nHi " + f"{user}," + " record your current mood\n"

mood_options = "\nDone = 1        Edit = 2       Delete = 3\n"
mood_edit_msg = "\nMood has been updated\n"
delete_msg = "\nMood deleted\n"

# Set Goal

goal_greeting = "\nHi " + f"{user}," + " set a goal and due date\n"

goals_options = "\nEdit = 1       Mark as completed = 2\n"

goals_edit_msg = "\nGoal has been updated\n"
completed_msg = "\nGoal completed\n"

# Exit

exit_msg = """
Ok, it sounds like you're done for today. 

Checking in regularly is helping you build habits. 

Come back tomorrow!
"""

# ____________________________________________________________________________
# MAIN PROGRAM
# ____________________________________________________________________________

print(co_name)
print(loading)
print(loading)
print(menu2)
menu2_choice = int(input("> "))
if menu2_choice == 1:
    print(loading)
    print(mood_greeting)
    date = str(input("> Today's date (dd-mm-yyyy): "))
    mood = str(input("> Today's mood: ")).lower()
    reason = str(input("> I feel this way because: "))
    user_moods = {
        "date": f"{date}",
        "mood": f"{mood}",
        "reason": f"{reason}"
    }
    collection1.insert_one(user_moods)
    print()
    print(collection1.find_one({"date": f"{date}"}))
    print(mood_options)
    mood_opt_choice = input("> ")
if menu2_choice == 2:
    print(loading)
    print(goal_greeting)
    date = str(input("> Today's date (dd-mm-yyyy): "))
    goal = str(input("> Today's goal: ")).lower()
    goal_due = str(input("> Due date (dd-mm-yyyy): "))
    user_goals = {
        "date": f"{date}",
        "goal": f"{goal}",
        "goal_due": f"{goal_due}"
    }
    collection2.insert_one(user_goals)
    print()
    print(collection2.find_one({"date": f"{date}"}))
    print(goals_options)
    goal_opt_choice = input("> ")
if menu2_choice == 3:
    print(exit_msg)
