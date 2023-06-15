# Task-Manager

Here's a breakdown of what the code does:

It imports the datetime module from the datetime library.

It reads the contents of a file named 'user.txt' and extracts the usernames and passwords from each line of the file. The usernames and passwords are stored in separate lists for later use in the login section.

It prompts the user to enter their username and password for login. It checks if the entered username is valid by comparing it to the usernames stored in the usernames list. If the username is valid, it prompts the user to enter their password and checks if the entered password is correct by comparing it to the password stored in the passwords list at the same index as the username.

If the login is successful, it displays a success message and proceeds to the next section.

The code defines several functions:

reg_user(): Prompts the user to enter a new username and password, checks if the username is already taken, confirms the password, and writes the new user information to the 'user.txt' file.
add_task(): Prompts the user to input task details and writes them to a file named 'tasks.txt'.
view_all(): Reads and prints the contents of the 'tasks.txt' file, displaying all task information in a formatted manner.
view_mine(): Allows a user to view only their tasks and modify tasks assigned to them from the 'tasks.txt' file.
view_stats(): Reads and prints the contents of two text files ('user_overview.txt' and 'task_overview.txt'), which provide an overview of user and task statistics.
task_overview(): Reads the 'tasks.txt' file, calculates various statistics related to the tasks (e.g., total tasks, completed tasks, overdue tasks), and writes the results to a new file ('task_overview.txt').
user_overview(): Generates an overview of tasks assigned to each user, including the total number of tasks assigned, the percentage of tasks assigned, completed, incomplete, and overdue.
generate_review(): Calls the task_overview() and user_overview() functions to generate review reports.
The code presents a menu to the user based on their username. If the username is "admin", additional options for registering a new user and viewing statistics are included in the menu. If the username is not "admin", the menu only includes options for adding a task, viewing all tasks, viewing the user's own tasks, and exiting the program.

Inside the menu loop, the code prompts the user to choose an option, and based on the input, it calls the corresponding function or performs the corresponding action.

If the user selects the "exit" option, the code displays a goodbye message and exits the program.

Overall, the code provides a basic task management system where users can log in, add tasks, view tasks, and perform other administrative tasks (if they have the necessary privileges).
