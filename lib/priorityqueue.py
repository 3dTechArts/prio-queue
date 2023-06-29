"""
Module: priorityqueue.py
Author: Reza Mousavi
Date: June 28th, 2023

This module provides classes for managing a priority queue of tasks.
"""
from datetime import datetime



class Task(dict):
    """
    Represents a task with a command and priority.

    This class inherits from the built-in `dict` class
    to provide a dictionary-like object.
    """    
    def __init__(self, command, priority):
        """
        Initializes a new Task object.

        Args:
            command (str): The command associated with the task.
            priority (int): The priority level of the tasks
                please provide any int between 0 to 10 
                10 will be the highest prio
                0 will be the lowest prio
        """
        self.update({"command": command, "priority": priority})


class PrioQueue:
    """
    Represents a priority queue for managing tasks in an order
    Tasks are ordered based on their priority and reception time.
    """    
    def __init__(self):
        """
        Initializes a new PrioQueue object.
        """        
        self.queue = []

    def __str__(self):
        """
        Here we are constructing a string representation
        of the PrioQueue object.

        Returns:
            str: A string representation of the PrioQueue object.
        """        
        output = ""
        for order_number, task in enumerate(self.queue):
            output += f"Order: {order_number+1} - Task: {task['command']}\n"
        return output

    def add_new_task(self, command, priority):
        """
        Adds a new task to the priority queue.

        Args:
            command (str): The command associated with the task.
            priority (int): The priority level of the task.

        Notes:
            - The task's reception time is automatically set to the current time.
            - The tasks in the queue are sorted based on their priority
                in descending order and their reception time in ascending order.
        """
        incoming_task = Task(command, priority)

        # Here we are adding a new key to the task onject
        # to be able to get track of the tasks reception time
        # to enable us to place them in the right order
        incoming_task["reception_time"] = datetime.now()
        self.queue.append(incoming_task)

        # Here we are sorting the tasks first based on their prio value
        # Sort the tasks by priority in descending order and reception 
        # time in ascending order. Negative sign (-) ensures higher priority 
        # tasks appear first regardless of zero or negative priority values
        self.queue = sorted(self.queue, key=lambda task:(-task["priority"], task["reception_time"]))
        


