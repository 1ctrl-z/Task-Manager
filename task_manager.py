#=====importing libraries===========
from datetime import datetime

#====Login Section====
# This code block is reading the contents of a file named 'user.txt' and extracting the usernames and
# passwords from each line of the file. It then stores the usernames and passwords in separate lists
# for later use in the login section of the code. The 'with open' statement is used to open the file
# and automatically close it when the block of code is finished executing.

with open('user.txt', 'r') as file_input:

    usernames = []
    passwords = []

    for data in file_input:
        username, password = data.strip().split(', ')
        usernames.append(username)
        passwords.append(password)

# This code block is responsible for prompting the user to enter their username and password for
# login. It checks if the entered username is valid by checking if it is present in the `usernames`
# list. If the username is invalid, it prints an error message and continues the loop. If the username
# is valid, it prompts the user to enter their password. It then checks if the entered password is
# correct by comparing it to the password stored in the `passwords` list at the same index as the
# username. If the password is incorrect, it prints an error message and continues the loop. If the
# password is correct, it prints a success message and breaks out of the loop, allowing the program to
# continue to the next section.
while True:
    input_username = input('Enter your username: ')

    if input_username not in usernames:
        print('Invalid username. Please try again.')
        continue

    password = input('Enter your password: ')
    password_index = usernames.index(input_username)

    if password != passwords[password_index]:
        print('Invalid password. Please try again.')
        continue

    print('\nLogin successful.')
    break

#====Defining Functions====
def reg_user():
    """
    This function prompts the user to enter a new username and password, checks if the username is
    already taken, confirms the password, and writes the new user information to a file.
    """
    incorrect_username = True
    while True:
        if incorrect_username:
            new_user = input("Please enter a username: ")
            if new_user in usernames:
                print("Username is taken, try again")
                continue
            else:
                incorrect_username = False

                new_user_pass = input("Please enter a password: ")
        confirm_password = input("Please confirm your password: ")

        if new_user_pass == confirm_password:
            print("\nNew user created successfully!")

            with open("user.txt", "a") as write_user:
                write_user.write(f"\n{new_user}, {new_user_pass}")

            break
            
        else:
            print("Passwords do not match, please try again")
            continue

def add_task():
    """
    This function prompts the user to input task details and writes them to a file named "tasks.txt".
    """
    task_details = [
            input("Enter the username of whom the task is assigned to: "),
            input("Enter the title of the task: "),
            input("Enter a description of the task: "),
            input("Enter the due date of the task: "),
            datetime.today().date().strftime("%d %b %Y"),
            "No"
            ]
    with open("tasks.txt", "a") as write_task:
        write_task.write("\n" + ", ".join(task_details))

def view_all():
    """
    The function reads and prints the contents of a file containing task information in a formatted
    manner.
    """
    with open('tasks.txt', 'r') as tasks_input:
            for data in tasks_input:
                data = data.strip().split(', ')
                print(f"\nTask: \t\t\t{data[1]}\n"
                      f"Assigned to: \t\t{data[0]}\n"
                      f"Date Assigned: \t\t{data[4]}\n"
                      f"Due Date: \t\t{data[3]}\n"
                      f"Task Complete? \t\t{data[5]}\n"
                      f"Task Description: \n {data[2]}")

def view_mine():
    """
    The function allows a user to view only their tasks and modify tasks assigned to them from a file.
    """
    with open('tasks.txt', 'r') as tasks_file:
        tasks = tasks_file.readlines()

    tasks_dict = {}
    for i, data in enumerate(tasks):
        task_details = data.strip().split(', ')
        tasks_dict[i+1] = task_details

    if input_username not in [task[0] for task in tasks_dict.values()]:
        print("You have no tasks assigned to you.")
    else:
        while True:
            print("\nThe following tasks are assigned to you:")
            for key, task in tasks_dict.items():
                if task[0] == input_username:
                    print(f"\n{key}. "
                          f"\nTask: \t\t\t{task[1]}\n"
                          f"Assigned to: \t\t{task[0]}\n"
                          f"Date Assigned: \t\t{task[4]}\n"
                          f"Due Date: \t\t{task[3]}\n"
                          f"Task Complete? \t\t{task[5]}\n"
                          f"Task Description: \n {task[2]}")

            task_selection = input("\nEnter the number of the8 task you want to select or enter '-1' to return to the main menu: ")
            
            if task_selection == '-1':
                break
            
            elif not task_selection.isdigit():
                print("Invalid input. Please enter a valid task number.")
                continue
                
            elif int(task_selection) not in tasks_dict.keys():
                print("Invalid input. Please enter a valid task number.")
                continue
                
            else:
                task_index = int(task_selection)
                task = tasks_dict[task_index]
                
                if task[5] == "Yes":
                    print("\nThis task has already been completed and cannot be modified.")
                    continue

                task_options = input("Enter '1' to mark the task as complete, '2' to edit the task or any other key to go back to the main menu: ")
                
                if task_options == '1':
                    tasks_dict[task_index][5] = "Yes"
                    with open('tasks.txt', 'w') as tasks_file:
                        for t in tasks_dict.values():
                            tasks_file.write(", ".join(t) + "\n")
                    print("Task marked as complete.")
                
                elif task_options == '2':
                    print(f"Selected Task: {task[1]}")
                    edit_options = input("Enter '1' to edit the assigned user, '2' to edit the due date: ")
                    
                    if edit_options == '1':
                        new_user = input("Enter the new assigned user: ")
                        tasks_dict[task_index][0] = new_user
                        with open('tasks.txt', 'w') as tasks_file:
                            for t in tasks_dict.values():
                                tasks_file.write(", ".join(t) + "\n")
                        print("Task updated.")
                    
                    elif edit_options == '2':
                        new_due_date = input("Enter the new due date (in the format 03 May 2023): ")
                        tasks_dict[task_index][3] = new_due_date
                        with open('tasks.txt', 'w') as tasks_file:
                            for t in tasks_dict.values():
                                tasks_file.write(", ".join(t) + "\n")
                        print("Task updated.")
                    
                    else:
                        print("You have selected an invalid option.")
                
                else:
                    print("You have selected an invalid option.")

def view_stats():
    """
    The function reads and prints the contents of two text files, one containing user overview and the
    other containing task overview.
    """
    try:
        with open('user_overview.txt', 'r') as users_input:
            print("\nUser Overview")
            for line in users_input:
                line = line.strip("\n")
                print(line)


        with open('task_overview.txt', 'r') as tasks_input:
            print("\nTask Overview")
            for line in tasks_input:
                line = line.strip("\n")
                print(line)
    except FileNotFoundError:
        generate_review()
        view_stats()


def task_overview():
    """
    The function reads a file containing task details, calculates various statistics related to the
    tasks, and writes the results to a new file.
    """
    with open('tasks.txt', 'r') as tasks_file:
        tasks = tasks_file.readlines()

    tasks_dict = {}
    for i, data in enumerate(tasks):
        task_details = data.strip().split(', ')
        current_task_user = task_details[0].strip()
        tasks_dict[i + 1] = task_details

    total_tasks = len(tasks_dict)
    completed_tasks = 0
    overdue_tasks = 0
    for task in tasks_dict.values():
        if task[5] == "Yes":
            completed_tasks += 1
        if datetime.strptime(task[4], '%d %b %Y').date() < datetime.today().date():
            overdue_tasks += 1
    incompleted_tasks = total_tasks - completed_tasks
    incomplete_percentage = round(incompleted_tasks / total_tasks * 100, 2)
    overdue_percentage = round(overdue_tasks / total_tasks * 100, 2)

    with open('task_overview.txt', 'w') as write_file:
        write_file.write(f"Total Tasks: {total_tasks}\n"
                         f"Completed Tasks: {completed_tasks}\n"
                         f"Overdue Tasks: {overdue_tasks}\n"
                         f"Incompleted Tasks: {incompleted_tasks}\n"
                         f"Incomplete Percentage: {incomplete_percentage}%\n"
                         f"OverDue Percentage: {overdue_percentage}%"
                         )

def user_overview():
    """
    This function generates an overview of tasks assigned to a specific user, including the total number
    of tasks assigned, the percentage of tasks assigned, completed, incomplete, and overdue.
    """

    found_task = False
    with open('tasks.txt', 'r') as tasks_file:
        tasks = tasks_file.readlines()
        tasks_dict = {}
        for i, data in enumerate(tasks):
            details = data.strip().split(', ')
            current_task_user = details[0].strip()
            tasks_dict[i+1] = details # store task details in dictionary
        total_tasks = len(tasks_dict)

    with open('user.txt', 'r') as users_file: # read user.txt file
        users = users_file.readlines()
        total_users = len(users)

    with open('user_overview.txt', 'w') as write_file:
        write_file.write(f"Total Users: {total_users}\n"
                         f"Total Tasks: {total_tasks}\n")

        for user in users:
            user = user.split(", ")[0]
            tasks_assigned = 0
            tasks_completed = 0
            tasks_overdue = 0
            incomplete_percentage = 0
            completed_percentage = 0
            overdue_percentage = 0
            for task in tasks_dict.values():
                if task[0] == user:
                    tasks_assigned += 1
                if task[0] == user and task[5].strip() == "Yes":
                    tasks_completed += 1
                if task[0] == user and datetime.strptime(task[4], '%d %b %Y').date() < datetime.today().date() and task[-1].strip() == "No":
                    tasks_overdue += 1
            tasks_incomplete = tasks_assigned - tasks_completed
            if tasks_assigned > 0:

                incomplete_percentage = round(tasks_incomplete / tasks_assigned * 100, 2)
                completed_percentage = round(tasks_completed / tasks_assigned * 100, 2)
                overdue_percentage = round(tasks_overdue / tasks_assigned * 100, 2)

            write_file.write(f"\nUser: {user}\n"
                            f"Total Tasks Assigned: {tasks_assigned}\n"
                            f"Percentage of Tasks Assigned: {100 / total_tasks * tasks_assigned:.2f}%\n"
                            f"Percentage of Completed Tasks: {completed_percentage}%\n"
                            f"Percentage of Incomplete Tasks: {incomplete_percentage}%\n"
                            f"Percentage of Overdue Tasks: {overdue_percentage}%\n")

def generate_review():
    """
    This function generates a review by calling two other functions, task_overview() and
    user_overview().
    """
    task_overview()
    user_overview()

# This code block is defining the menu options that will be presented to the user based on their
# username. If the username is "admin", the menu will include additional options for registering a new
# user and viewing statistics. If the username is not "admin", the menu will only include options for
# adding a task, viewing all tasks, viewing the user's own tasks, and exiting the program.
if input_username == "admin":
    menu_ = '''\nSelect one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : '''

else:
    menu_ = '''\nSelect one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : '''

while True:

    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input(menu_).lower()

    
    if menu == 'r' and input_username == "admin":
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'ds' and input_username == "admin":
        view_stats()

    elif menu == 'gr'and input_username == "admin":
        generate_review()

    elif menu == 'e':

        # This code block is checking if the user input is 'e' (for exit) and if it is, it prints the
        # message "Goodbye!!!" and exits the program using the `exit()` function.
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")