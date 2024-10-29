# Keysight-CLI

Keysight-CLI is a command-line interface tool for managing tasks. It offers different functionalities to add, complete, and delete tasks in single-task or multi-task modes.

## Branches Overview

This repository contains two branches, `Draft-1` and `Draft-2`, each with different functionalities under the `main` branch.

### Branches

- **Draft-1**: Contains `task_manager.py`, which supports single-task operations.
  - **Features**:
    - Add a single task
    - Complete a single task
    - Delete a single task

- **Draft-2**: Contains `multiTask_manager.py`, which supports multiple-task operations.
  - **Features**:
    - Add multiple tasks at once
    - Complete multiple tasks at once
    - Delete multiple tasks at once

# Keysight-CLI: Task Manager

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
