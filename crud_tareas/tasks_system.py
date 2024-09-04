'''
TASKS SYSTEM
'''
import time
from tasks import *

def main():
    user = input('User: ')
    task_list = load_tasks_from_json()

    while True:
        print(f'\nWelcome {user}!')
        print('\n----- OPTION MENU -----')
        print('1. View Tasks\n2. Add Task\n3. Search Task\n4. Update Task\n5. Delete Task\n6. Exit')

        try:
            opc = int(input('Option: '))
        except ValueError:
            print("\nInvalid option! Please, enter the correct option.\n")
            continue

        if opc == 1:
            show_tasks(task_list)
        elif opc == 2:
            add_task(task_list)
        elif opc == 3:
            if task_list:
                result = search_task(task_list)
                if result:
                    print(f'The task found is: {result}')
            else:
                print('Task not found. Register a task first.')
        elif opc == 4:
            try:
                task_index = int(input('Index: ')) - 1
                new_task = input('New Task: ')
                result = update_task(task_list, 
                                     new_task, 
                                     task_index)

                if result:
                    print('\nUpdated task!\n')
                else:
                    print('\nInvalid index!\n')
            except ValueError:
                print("\nInvalid option! Please, enter the correct option.\n")
                time.sleep(5)
        elif opc == 5:
            try:
                task_index = int(input('Index: ')) - 1
                result = delete_task(task_list, task_index)

                if result:
                    print('\nDeleted task!\n')
                else:
                    print('\nInvalid index!\n')
            except ValueError:
                print("\nInvalid option! Please, enter the correct option.\n")
                time.sleep(5)
        elif opc == 6:
            print(f'\nGoodbye {user}!\n')
            break
        else:
            print("\nInvalid option! Please, enter the correct option.\n")
            time.sleep(5)

if __name__ == "__main__":
    main()

