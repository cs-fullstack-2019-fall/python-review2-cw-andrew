def prob1():
    import pickle

    print(f"Congratulations! You're running Christian's and Andrew's Task list program.")
    print(" ")
    userInput = print("What would you like to do next?")
    taskforce = []

    while userInput != "0":
        userInput = input(f"# 1. List all tasks.\n"
              f"# 2. Add a task to the list.\n"
              f"# 3. Delete a task.\n"
              f"# 0. To quit the program\n")
        if userInput == "1":
            taskfile = "Task_File.py"
            with open(taskfile) as f:
                taskforce = f.readlines()
            input("Press 'f' to open file")

            print(taskforce)

        elif userInput == "2":
            from index2 import add_task
            add_task(taskforce)

        elif userInput == "3":
            from index2 import delete_task
            delete_task(taskforce)
