import os
import json

def search_task(task_list):
    entrance = input('Enter the word or index: ')

    if entrance.isdigit():
        num_task = int(entrance)

        if 1 <= num_task <= len(task_list):
            return task_list[num_task - 1]
        else:
            print('Number out of range!')
            return None
    else:
        searched_task = entrance.lower()
        coincidences = [task for task in task_list if searched_task in task.lower()]

        if coincidences:
            print(f"Matches found: {', '.join(coincidences)}")
        else:
            print(f'No match found for {entrance}.')

        return None

def save_tasks_to_json(task_list):
    with open('task_info.json', 'w', encoding='utf-8') as file:
        data = {str(i + 1): task for i, task in enumerate(task_list)}
        json.dump(data, 
                  file, 
                  ensure_ascii=False, 
                  indent=4)

def load_tasks_from_json():
    if os.path.exists('task_info.json'):
        with open('task_info.json', 'r', encoding='utf-8', errors='replace') as file:
            return list(json.load(file).values())
    return []

def show_tasks(task_list):
    if not task_list:
        print('\nNo tasks registered!\n')
    else:
        print('\n---- TASK LIST ----')
        for index, task in enumerate(task_list):
            print(f'{index + 1}. {task}')

def add_task(task_list):
    try:
        num_tasks = int(input('Enter the number of tasks:  '))
        if num_tasks < 1:
            raise ValueError('The amount of tasks must be positive!')

        for i in range(num_tasks):
            new_task = input(f'Enter task {i + 1}: ')
            task_list.append(new_task)

        save_tasks_to_json(task_list)
        print(f'\n{num_tasks} task(s) registered!\n')
    except ValueError as e:
        print(f'Invalid input: {e}')

def update_task(task_list, new_task, index):
    if 0 <= index < len(task_list):
        task_list[index] = new_task
        save_tasks_to_json(task_list)
        return True
    else:
        return False

def delete_task(task_list, index):
    if 0 <= index < len(task_list):
        task_list.pop(index)
        save_tasks_to_json(task_list)
        return True
    else:
        return False


