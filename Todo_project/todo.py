class Todo():
    def __init__(self):
        # a statment to greeet and introduce the user to our application
        self.welcome = ""
        # a list holding all tasks in place
        self.alltask = []

    
    def create(self):
        # requesting task name and time from user
        task_name = str(input("What task do you perform: "))
        task_time = str(input("At what time do you what to carry ot task: ")) 
        # CREATING THE TASK
        task_row = {"task_id":len(self.alltask), "task_name": task_name, "task_status": "Not Done", "task_time": task_time }
        self.alltask.append(task_row)
        
    def Read(self):
        pass
    def update(self):
        # initializing a variable to hold the task_id of the task to be marked done
        Boo = True
        while Boo:
            task_id = input("What task number are you trying to change: ")
            if task_id.isdigit() and task_id in range(1,len(self.alltask)+1):
                Boo = False
            else:
                print("This input is not an integer")
                continue
        print(f"The status of this task is currently:{self.alltask[task_id]['task_status']}")

        # this while loop will ensure the user wants to perform change as well as perform checks on user input

        while True:
            x = input("Do you want to go ahead and change status: Y or N")
            if x.capitalize() == "Y":
                self.alltask[task_id]["task_status"] = "Done"
                print(f"The status of the task {self.alltask[task_id]['task_name']} has been updated to {self.alltask[task_id]['task_status']} ")
                break
            elif x.capitalize() == "N":
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


gochi = Todo()

gochi.create()