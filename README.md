# Keysight-CLI: Task Manager

Keysight-CLI is a command-line tool for efficiently managing your tasks. Easily add, view, complete, and delete tasks directly from the terminal.

## Available Commands

Below are the commands to manage tasks with `task_manager.py`:

### 1. Add a Task
- **Command**: `task_manager.py Add "<Task Name>" "<Task Description>"`
- **Example**:
  ```shell
  python3 task_manager.py Add "Buy Groceries" "Lentils, Spices, Vegetables"

### 2. View The Tasks
- **Command**: `task_manager.py View`
- **Example**:
  ```shell
  python3 task_manager.py View

### 3. Complete The Task
- **Command**: `task_manager.py Complete <Task_Number>`
- **Example**:
  ```shell
  python3 task_manager.py Complete 1
  
### 4. Delete The Task
- **Command**: `task_manager.py Delete <Task_Number>`
- **Example**:
  ```shell
  python3 task_manager.py Delete 1
