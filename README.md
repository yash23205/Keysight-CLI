# Keysight-CLI: Task Manager

Keysight-CLI is a command-line tool for efficiently managing your tasks. Easily add, view, complete, and delete tasks directly from the terminal.

## Available Commands

Below are the commands to manage tasks with `multiTask_manager.py`:

### 1. Add Multiple Tasks
- **Command**: `multiTask_manager.py Add "<Task Name 1>" "<Task Description 1>" "<Task Name 2>" "<Task Description 2>" "<Task Name 3>" "<Task Description 3>"`
- **Example**:
  ```shell
  python3 multiTask_manager.py Add "Buy Groceries" "Lentils, Spices, Vegetables" "Buy Cars" "Mercedes,G-Wagon" "Pay Bills" "Electricity,Water"

### 2. View The Tasks
- **Command**: `multiTask_manager.py View`
- **Example**:
  ```shell
  python3 multiTask_manager.py View

### 3. Complete Multiple Tasks
- **Command**: `multiTask_manager.py Complete <Task_Number 1> <Task_Number 2> <Task_Number 3>`
- **Example**:
  ```shell
  python3 multiTask_manager.py Complete 1 2 3
  
### 4. Delete Multiple Tasks
- **Command**: `task_manager.py Delete <Task_Number 1> <Task_Number 2> <Task_Number 3>`
- **Example**:
  ```shell
  python3 task_manager.py Delete 1 2 3
