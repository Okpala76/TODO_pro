import smtplib
from email.message import EmailMessage

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
        ### th
        self.mail = self.mail_collector()


    def create(self):
        # requesting task name and time from user
        task_name = input("What task do you want to perform: ")  #!input always give strings as output. ## Okay corrected
        task_time = input("At what time do you what to carry out said task: ") 
        # CREATING THE TASK
        task_row = {"task_id":len(self.alltask)+1, "task_name": task_name, "task_status": "Not Done", "task_time": task_time } #! i edited task id and added +1, so that the id of every new task will be higer than d last
        self.alltask.append(task_row)

        ### wrote the code message for the mail alert
        create_subject = f"Task Created!!!! :{task_name} "
        create_body = f"Your task '{task_name}' has been created and should be done by {task_time} "

        ### The mail fuction being called in the create method
        self.mail_reminder(create_subject, create_body)
        
    def read(self):
        for todo_items in self.alltask:
            print(f'''
{todo_items['task_id']}.] TASK: {todo_items['task_name']}    STATUS:{todo_items['task_status']}     PERIOD DUE:{todo_items['task_time']}''') 

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
        task__name = self.alltask[int(task_id)-1]['task_name']
        task__status = self.alltask[int(task_id)-1]['task_status']

        while True:
            x = input("Do you want to go ahead and change status: Y or N")
            if x.capitalize() == "Y":
                task__status = "Done"
                print(f"The status of the task {task__name} has been updated to {task__status} ")
                break
            elif x.capitalize() == "N":
                print("you've exited the update command, Type update to try again")
                break
            else:
                print("The value inputted is not a 'Y' or 'N': Try again....")
                continue  
            
        ## calling the mail function again to alert on update  
        update_subject = "Your task: " + task__name
        update_body = "The status of your task "+ task__name +" has been updated to " + task__status
        
        self.mail_reminder(update_subject, update_body)

        print(update_body)


    def delete(self):
        #gets id of  task to be deleted:
        cascade_task = int (input('input id of item to be deleted: '))
        index = 0
        for tasks in self.alltask:
            #index of alltask list
            
            if cascade_task == tasks['task_id']:
                print(f"task id:{tasks['task_id']}selected")
                del self.alltask[index]
                print(f"task id:{tasks['task_id']} deleted")
                break
                
            else:
                index += 1

        #update task id after delete.
        update_id = 1
        for tasks in self.alltask:
            tasks['task_id'] = update_id
            update_id +=1
        print('todo_list id updated')
        
    def time(self):
        pass
    
    ## mail collector: This collect the users mail 
    def mail_collector(self):
        while True:
            email = input("Please provide an email for alerts: ")
            con_email = input("Please confirm mail: ")

            if email != con_email:
                print("Please try again, the your mail does not tally")
                continue
            else:
                break   
        return email

    ## mail_reminder: This bears the email interaction function
    def mail_reminder(self,task_subject,task_message):

        def email_alert(subject, body,to):
            msg = EmailMessage()
            msg.set_content(body)
            msg['subject'] =subject
            msg['to'] = to

            user = "mathprix5@gmail.com"
            msg['from'] = user
            password = "lwbpreoktpqlzzsz"

            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(user, password)
            server.send_message(msg)

            server.quit()

        email_alert(task_subject, task_message,self.mail)