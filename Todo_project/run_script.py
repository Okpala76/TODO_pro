from todo import Todo




#Regulates smooth runing of the app from the cli interface.
def run ():
    todo_app = Todo()

    print(todo_app.manual)
    # runs the todo program 
    while True:
        command = input('write your command here: ')
        if command == 'create':
            todo_app.create()
    
        elif command == 'update':
            todo_app.update()
        
        elif command == 'read':
            todo_app.read()

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
run()