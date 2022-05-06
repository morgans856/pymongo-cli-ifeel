import json

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

mood_options = "\nDone = 1      Delete = 2\n"
mood_edit_msg = "\nMood has been updated\n"
delete_msg = "\nMood deleted\n"

# Set Goal

goal_greeting = "\nHi " + f"{user}," + " set a goal and due date\n"

goals_options = "\nDone = 1     Edit due date = 2\n"

goals_edit_msg = "\nDue date has been updated\n"
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
while menu2_choice == 1 or 2 or 3:
    if menu2_choice == 1:
        print(loading)
        print(mood_greeting)
        date = str(input("> Today's date (dd/mm/yyyy): "))
        mood = str(input("> Today's mood: "))
        reason = str(input("> I feel this way because: "))
        user_moods = {
            "date": f"{date}",
            "mood": f"{mood}",
            "reason": f"{reason}"
        }
        collection1.insert_one(user_moods)
        print()
        print(json.dumps(collection1.find_one({"date": f"{date}", "mood": f"{mood}"}, {"_id": 0})))
        print(mood_options)
        mood_opt_choice = int(input("> "))
        if mood_opt_choice == 2:
            collection1.delete_one({"date": f"{date}", "mood": f"{mood}"})
            print(delete_msg)
            print(loading)
            print(loading)
            print(menu2)
            menu2_choice = int(input("> "))
        if mood_opt_choice == 1:
            print(loading)
            print(loading)
            print(menu2)
            menu2_choice = int(input("> "))
    if menu2_choice == 2:
        print(loading)
        print(goal_greeting)
        date = str(input("> Today's date (dd/mm/yyyy): "))
        goal = str(input("> Today's goal: ")).lower()
        goal_due = str(input("> Due date (dd/mm/yyyy): "))
        user_goals = {
            "date": f"{date}",
            "goal": f"{goal}",
            "goal_due": f"{goal_due}"
        }
        collection2.insert_one(user_goals)
        print()
        print(json.dumps(collection2.find_one({"date": f"{date}", "goal": f"{goal}"}, {"_id": 0})))
        print(goals_options)
        goal_opt_choice = int(input("> "))
        if goal_opt_choice == 2:
            print()
            new_goal_due = str(input("> New due date (dd/mm/yyyy): "))
            print()
            collection2.update_one({"date": f"{date}", "goal": f"{goal}"}, {"$set": {"goal_due": f"{new_goal_due}"}})
            print(json.dumps(collection2.find_one({"date": f"{date}", "goal": f"{goal}"}, {"_id": 0})))
            print()
            print(goals_edit_msg)
            print(loading)
            print(loading)
            print(menu2)
            menu2_choice = int(input("> "))
        if goal_opt_choice == 1:
            print(loading)
            print(loading)
            print(menu2)
            menu2_choice = int(input("> "))
    if menu2_choice == 3:
        print(exit_msg)
        break
