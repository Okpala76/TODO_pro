class Todo():
    def __init__(self):
        # a statment to greet and introduce the user to our application
        self.welcome = print ("""
        Welcome to  Todo.
        You have taken the first step towards getting your life organised and achieving your goals. 
        This app is designed to help you prioritise your tasks, stay focused, and boost your productivity.

        With Todo, you can:
        - Create and manage your to-do lists with ease.
        - Set reminders and due dates to stay on track.
        - Track your progress and celebrate your accomplishments.
        - Stay organised and focused on what matters most. 
                             
        Let's get started and amke today count.
        """)
        
        # a list holding all tasks in place
        self.alltask = []

        #a variable holding all commands 
        self.manual ='''
        Commands: 
            create ----- To create todo item
            update ----- To update todo lsit
            read   ----- To view created tasks
            exit   ----- To exit todo list
            view   ----- To view todo items
            help   ----- To view manual
            '''



    def create(self):
        # requesting task name and time from user
        task_name = str(input("What task do you want to perform: "))  #!input always give strings as output.
        task_time = str(input("At what time do you what to carry out said task: ")) 
        # CREATING THE TASK
        task_row = {"task_id":len(self.alltask)+1, "task_name": task_name, "task_status": "Not Done", "task_time": task_time } #! i edited task id and added +1, so that the id of every new task will be higer than d last
        self.alltask.append(task_row)
        
    def read(self):
        for todo_items in self.alltask:
            print(todo_items) 

    def update(self):
        # initializing a variable to hold the task_id of the task to be marked done

        while True:
            task_id = input("What task number are you trying to change: ")
            if task_id.isdigit() and int(task_id) in range(1,len(self.alltask)+1):
                break
            else:
                print("This input is not an integer or out of range")
                continue

        print(f"The status of this task is currently:{self.alltask[int(task_id)-1]['task_status']}")

        # this while loop will ensure the user wants to perform change as well as perform checks on user input

        while True:
            x = input("Do you want to go ahead and change status: Y or N")
            if x.capitalize() == "Y":
                self.alltask[int(task_id)-1]["task_status"] = "Done"
                print(f"The status of the task {self.alltask[int(task_id)-1]['task_name']} has been updated to {self.alltask[int(task_id)-1]['task_status']} ")
                break
            elif x.capitalize() == "N":
                print("you've exited the update command, Type update to try again")
                break
            else:
                print("The value inputted is not a 'Y' or 'N': Try again....")
                continue  
        


    def delete(self):
        pass
    def time(self):
        pass
    def mail_reminder(self):
        pass









