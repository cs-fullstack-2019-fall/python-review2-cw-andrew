def prob1():
    import pickle

    print(f"Congratulations! You're running Christian's and Andrew's Task list program.")
    print(" ")
    userInput = ""
    taskforce = []

    while userInput != "0":
        userInput = input(f"# 1. List all tasks.\n"
              f"# 2. Add a task to the list.\n"
              f"# 3. Delete a task.\n"
              f"# 0. To quit the program\n")
        if userInput == "1":
            for eachElement in taskforce:
                print(eachElement)

        elif userInput == "2":
            from index2 import add_task
            add_task(taskforce)

        elif userInput == "3":
            from index2 import delete_task
            delete_task(taskforce)

    f = open("saved_tasks.txt", "a")
    for eachElement in taskforce:
        f.write(f"{eachElement}\n")
    f.close()
