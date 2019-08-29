# Congratulations! You're running [YOUR NAME]'s Task List program.
#
# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program
# ```

# def prob1():
import pickle
#
# print(f"Congratulations! You're running Christian's and Andrew's Task list program.")
# print(" ")
# userInput = input("What would you like to do next? Press Enter.")
# taskforce = []
#
# while userInput != "0":
#     print(f"# 1. List all tasks.\n"
#           f"# 2. Add a task to the list.\n"
#           f"# 3. Delete a task.\n"
#           f"# 0. To quit the program\n")
#     userInput = input("What would you like to do? ")
#     if userInput == "1":
#         taskfile = "Task_File.py"
    #
    # with open(taskfile) as f:
    #     taskforce = f.readlines()
    #
    # print(taskforce)
    #
    # if taskforce != [""]:
    #     print("Please enter a task.")
    #     userInput = ("What would you like to do? Press enter. ")

#   elif userInput =="2":
#         add_Task
#   elif userInput == "3":
#         delete_task


#
#

if taskforce != [""]:
    print("Please enter a task.")
    userInput = ("What would you like to do? Press enter. ")

else:
    taskfile= "Task_File.py"
    print("")
    with open(taskfile) as f:
        taskforce = f.readlines()

    print(taskforce)

