from todo import Todo
import threading

# runs the todo program 
def todo_generator():
    todo_app = Todo()

    print(todo_app.manual)

    while True:
        command = input('write your command here: ')
        if command == 'create':
            todo_app.create()
    
        elif command == 'update':
            todo_app.update()
        
        elif command == 'read':
            todo_app.read()
        elif command == 'delete':
            todo_app.delete()
        elif command == 'help':
            print(todo_app.manual)
        elif command == 'exit':
            break
        else:
            print("""
            command does not exist.
            type 'help' to see commands.
            
            """)

#Regulates smooth runing of the app from the cli interface.
def run ():
    todo_app = Todo()
    while True:
        command = input('write your command here: ')
        if command == 'create':
            # Create threads
            t1 = threading.Thread(target= todo_app.create)
            t2 = threading.Thread(target= todo_generator)
            # Start threads
            t1.start()
            t2.start()
            
            # Wait for both threads to complete
            t1.join()
            t2.join()
    
        elif command == 'update':
            todo_app.update()
        
        elif command == 'read':
            todo_app.read()
        elif command == 'delete':
            todo_app.delete()
        elif command == 'help':
            print(todo_app.manual)
        elif command == 'exit':
            break
        else:
            print("""
            command does not exist.
            type 'help' to see commands.
            
            """)
    

            
            

# runs the Todo class
#run()
