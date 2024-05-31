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
        pass
    def delete(self):
        pass
    def time(self):
        pass
    def mail_reminder(self):
        pass
