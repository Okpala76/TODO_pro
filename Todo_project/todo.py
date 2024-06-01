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
        task_name = str(input("What task do you perform: "))  #!input always give strings as output.
        task_time = str(input("At what time do you what to carry ot task: ")) 
        # CREATING THE TASK
        task_row = {"task_id":len(self.alltask) + 1, "task_name": task_name, "task_status": "Not Done", "task_time": task_time } #! i edited task id and added +1, so that the id of every new task will be higer than d last
        self.alltask.append(task_row)
        
    def read(self):
        for todo_items in self.alltask:
            print(todo_items) 
    def update(self):
        self.create()

    def delete(self):
        pass
    def time(self):
        pass
    def mail_reminder(self):
        pass











