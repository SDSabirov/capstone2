#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
#program will read and store all authentication credetials on "login_auth"
login_auth=[]
with open('user.txt','r') as f:
    for line in f:
        line=line.replace(",","").split()
        login_auth.append(line)

is_admin=False          #when entering user name it will establish if user is admin or not

is_authorised=False     #to establish entered credentials 

counter=5               #counter to iterate attempts,user will have 4 attempts

while counter>0:
    #User enters user name and password
    user_name=input("Enter your user name:  ")
    password=input("Enter your password: ")

    #comparing username with usernames in login_auth
    for username_auth,password_auth in login_auth:
         #if both username and password exists
        if user_name==username_auth and password==password_auth:
            #if user entered with admin credentials 
            if user_name=='admin':
                is_admin=True

            
            is_authorised=True

            counter=0       #to stop while loop

    #esle while loop will keep asking for another attempts
    if is_authorised==False:
        print(f"Invalid credentials you have {counter-1} attempts left ")
        
    counter-=1

#if login was successful
if is_authorised:
    print("Login Successful!")

    while True:
        #presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        
        if is_admin:
            menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    stat - view statistics
    e - Exit
    : ''').lower()
        else:
            menu = input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()

        if menu == 'r':
            '''In this block you will write code to add a new user to the user.txt file
            - You can follow the following steps:
                - Request input of a new username
                - Request input of a new password
                - Request input of password confirmation.
                - Check if the new password and confirmed password are the same.
                - If they are the same, add them to the user.txt file,
                - Otherwise you present a relevant message.'''
            #only admin can register new user

            if is_admin:
                new_username=input("Enter a new username: ").lower()
                password=input("Enter your password: ")
                confirm_password=input("Confirm your password: ")

                if password==confirm_password:
                    with open('user.txt','a') as f:
                        f.write(f"\n{new_username}, {password}")
                        print("Credentials saved\n")
                else:
                    print("Passwords doesn't match\n")
            else:
                print("Access denied please login as admin! ")

        elif menu == 'a':
            
            '''In this block you will put code that will allow a user to add a new task to task.txt file
            - You can follow these steps:
                - Prompt a user for the following: 
                    - A username of the person whom the task is assigned to,
                    - A title of a task,
                    - A description of the task and 
                    - the due date of the task.
                - Then get the current date.
                - Add the data to the file task.txt and
                - You must remember to include the 'No' to indicate if the task is complete.'''
            #input for new task form    
            username=input("Please enter a username: ")
            title=input("Enter a title of the task: ")
            description=input("In few words, describe what is the task about: ")
            registration_date=date.today()
            registration_date=registration_date.strftime("%d %B %Y")    #formating date as %d-day %B-month in words %Y-year in 4 digits
            deadline=input("Enter end date dd Month yyyy: ")
            task_completion=input("Task completion status yes/no: ").capitalize()

            #opening file tasks.txt
            with open('tasks.txt','a') as f:
                #storing variables with appropriate formatting
                f.write(f"\n{username}, {title}, {description}, {registration_date}, {deadline}, {task_completion}")
            
            print("Task successfully saved! ")
        
        elif menu == 'va':
            
            '''In this block you will put code so that the program will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
                - Read a line from the file.
                - Split that line where there is comma and space.
                - Then print the results in the format shown in the Output 2 
                - It is much easier to read a file using a for loop.'''
            #opening tasks.txt
            with open('tasks.txt','r') as f:

                for line in f:

                    line=line.split(", ")   #splitting by coomma and space
                    #printing varibales in requared format
                    print("_"*80)
                    print(f"Task:\t\t{line[1]}")
                    print(f"Assigned to:\t{line[0]}")
                    print(f"Date Assigned:\t{line[3]}")
                    print(f"Due date:\t{line[4]}")
                    print(f"Task Complete?\t{line[5]}")
                    print(f"Task description:\n  {line[2]}")    
                    print("_"*80)

        elif menu == 'vm':
            
            '''In this block you will put code the that will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the username you have
                read from the file.
                - If they are the same print it in the format of Output 2 in the task PDF'''
            
            
            with open('tasks.txt','r') as f:

                for line in f:

                    line=line.split(", ")
                    #if user_name same as logged in user , print relative tasks
                    if line[0]==user_name:

                        print("_"*80)
                        print(f"Task:\t\t{line[1]}")
                        print(f"Assigned to:\t{line[0]}")
                        print(f"Date Assigned:\t{line[3]}")
                        print(f"Due date:\t{line[4]}")
                        print(f"Task Complete?\t{line[5]}")
                        print(f"Task description:\n  {line[2]}")    
                        print("_"*80)

        elif menu == 'stat':
            
            #only admin can see stats
            if is_admin:
                
                number_of_tasks=0
                number_of_users=0

                #counting number of tasks 
                with open('tasks.txt','r') as f:

                    for line in f:

                        number_of_tasks +=1

                #counting number of users        
                with open('user.txt','r') as f:

                    for line in f:
                        number_of_users +=1

                #printing results        
                print("_"*50)
                print(f"Number of tasks: {number_of_tasks}")
                print(f"Number of users: {number_of_users}")
                print("_"*50)


        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")