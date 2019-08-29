def add_task(any_list):
    user_add_task = input("Enter a task you would like to add to the list: ")
    any_list.append(user_add_task)


def delete_task(any_list):
    user_del_task = input("Enter a task you would like to delete from the list: ")
    if user_del_task in any_list:
        del_index = any_list.index(user_del_task)
        del any_list[del_index]


