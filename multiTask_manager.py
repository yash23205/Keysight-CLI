import sys
import os
from datetime import datetime

TASKS_FILE = "multitasks.txt"
PENDING_LIST = []
COMPLETED_LIST = []

# TASK CLASS
class Task:
    def __init__(self, name, description):
        # User Attributes
        self.name = name
        self.description = description

        # Generated Attributes
        self.date_assigned = datetime.now().strftime("%Y-%m-%d")
        self.time_assigned = datetime.now().strftime("%H:%M:%S")
        self.task_id = self.generate_task_id()
        self.task_number = 0
        self.completed = False
        self.date_completed = None
        self.time_completed = None

    def generate_task_id(self):
        current_time = datetime.now()
        task_id = current_time.hour + current_time.minute + current_time.second
        return f"{task_id:06}"
    
    def mark_completed(self):
        self.completed = True
        self.date_completed = datetime.now().strftime("%Y-%m-%d")
        self.time_completed = datetime.now().strftime("%H:%M:%S")


# TASK MANAGER: ADD / VIEW / DELETE / COMPLETE
class TaskManager:
    def __init__(self):
        self.load_tasks()

    # Updates The Global Complete List And Pending List
    def load_tasks(self):
        PENDING_LIST.clear()
        COMPLETED_LIST.clear()
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                current_list = None
                for line in file:
                    line = line.strip()
                    if line == "-------------------------------PENDING-------------------------------------------------":
                        current_list = PENDING_LIST
                        continue
                    elif line == "--------------------------------COMPLETED-----------------------------------------------":
                        current_list = COMPLETED_LIST
                        continue
                
                    if not line or current_list is None:
                        continue

                    try:
                        task_number, task_id, name, description, date, time, completed_flag = line.split(" | ")
                        task = Task(name.strip(), description.strip())
                        task.task_id = task_id.strip()
                        task.task_number = int(task_number.strip())
                        completed_flag = completed_flag.strip()
                    
                        if completed_flag == "True":
                            task.completed = True
                            task.date_completed = date.strip()
                            task.time_completed = time.strip()
                            COMPLETED_LIST.append(task)
                        else:
                            task.completed = False
                            task.date_assigned = date.strip()
                            task.time_assigned = time.strip()
                            PENDING_LIST.append(task)
                        
                    except ValueError:
                        pass

    # Helper Function To Save Tasks In tasks.txt File
    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            # For Pending Tasks
            file.write(f"-------------------------------PENDING-------------------------------------------------\n[TASK_NUMBER]  |  [TASK_ID] | [TASK_NAME] | [TASK_DESCRIPTION] | [DATE_ASSIGNED] | [TIME_ASSIGNED] | [FLAG]\n\n")
            for i, task in enumerate(PENDING_LIST):
                task.task_number = i
                file.write(f"{task.task_number}  |  {task.task_id} | {task.name} | {task.description} | {task.date_assigned} | {task.time_assigned}  |  {task.completed}\n")

            # For Completed Tasks
            file.write("\n--------------------------------COMPLETED-----------------------------------------------\n[TASK_NUMBER]  |  [TASK_ID] | [TASK_NAME] | [TASK_DESCRIPTION] | [DATE_COMPLETED] | [TIME_COMPLETED]\n\n")
            for i, task in enumerate(COMPLETED_LIST):
                task.task_number = i
                file.write(f"{task.task_number}  |  {task.task_id} | {task.name} | {task.description} | {task.date_completed} | {task.time_completed} | {task.completed}\n")

    # ADD MULTIPLE TASKS
    def add_tasks(self, tasks):
        for name, description in tasks:
            task = Task(name, description)
            PENDING_LIST.append(task)
        self.save_tasks()
        print("Tasks have been saved in the tasks.txt file")

    # LIST TASKS
    def list_tasks(self):
        if not os.path.exists(TASKS_FILE):
            print("No tasks.txt File Found")
            return

        with open(TASKS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line == "-------------------------------PENDING-------------------------------------------------":
                    print("-------------------------------PENDING-------------------------------------------------\n[TASK_NUMBER]  |  [TASK_ID] | [TASK_NAME] | [TASK_DESCRIPTION] | [DATE_ASSIGNED] | [TIME_ASSIGNED] | [FLAG]\n\n")
                    continue
                elif line == "--------------------------------COMPLETED-----------------------------------------------":
                    print("\n--------------------------------COMPLETED-----------------------------------------------\n[TASK_NUMBER]  |  [TASK_ID] | [TASK_NAME] | [TASK_DESCRIPTION] | [DATE_COMPLETED] | [TIME_COMPLETED] [FLAG]\n\n")
                    continue

                if not line or "TASK_NUMBER" in line:
                    continue

                try:
                    number, task_id, name, description, date, time, flag= line.split(" | ")
                    print(f"{number.strip()} | {task_id.strip()} | {name.strip()} | {description.strip()} | {date.strip()} | {time.strip()}  |  {flag.strip()}")
                except ValueError:
                    continue
    
    # COMPLETE MULTIPLE TASKS
    def complete_tasks(self, task_numbers):
        for task_number in task_numbers:
            flag=False
            for task in PENDING_LIST:
                if task.task_number == task_number:
                    task.mark_completed()
                    PENDING_LIST.remove(task)
                    COMPLETED_LIST.append(task)
                    print(f"TASK_NUMBER {task_number} Added To Complete List")
                    flag=True
                    break
            if(flag==False):
                print(f"TASK_NUMBER {task_number} ABSENT FROM THE PENDING LIST")
        self.save_tasks()

    # DELETE MULTIPLE TASKS   
    def delete_tasks(self, task_numbers):
        for task_number in task_numbers:
            flag_complete=False
            flag_pending=False
            for task in COMPLETED_LIST:
                if task.task_number == task_number:
                    COMPLETED_LIST.remove(task)
                    print(f"Task {task_number} Has Been Deleted From The Completed List")
                    flag_complete=True
                    break
            if flag_complete==True:
                continue
            for task in PENDING_LIST:
                if task.task_number == task_number:
                    print("WARNING : Task Is Pending Please Complete The Task")
                    flag_pending=True
                    break
            if flag_pending==True:
                continue
            print("Task Not Found")
        self.save_tasks()


# CLI Class For Commands
class CLI:
    def __init__(self):
        self.manager = TaskManager()

    def run(self):
        if len(sys.argv) < 2:
            print("Refer To ReadMe File In The GitHub To Understand The Use Of Commands")
            return

        command = sys.argv[1]
        # ADD MULTIPLE COMMAND
        if command == "Add" and len(sys.argv) > 3:
            tasks = [(sys.argv[i], sys.argv[i + 1]) for i in range(2, len(sys.argv), 2)]
            self.manager.add_tasks(tasks)
            
        # LIST COMMAND
        elif command == "View":
            self.manager.list_tasks()
            
        # COMPLETE MULTIPLE COMMAND
        elif command == "Complete" and len(sys.argv) > 2:
            task_numbers = [int(num) for num in sys.argv[2:]]
            self.manager.complete_tasks(task_numbers)
            
        # DELETE MULTIPLE COMMAND
        elif command == "Delete" and len(sys.argv) > 2:
            task_numbers = [int(num) for num in sys.argv[2:]]
            self.manager.delete_tasks(task_numbers)
            
        else:
            print("Invalid Command Refer To Github To Understand The Use Of Commands")


# MAIN FUNCTION
if __name__ == "__main__":
    cli = CLI()
    cli.run()
