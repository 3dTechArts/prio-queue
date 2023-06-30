# prio-queue
This repository provides a priority queue library for managing tasks based on their priority levels. 
The library allows you to add tasks with different priorities and retrieves them in the desired order.

## Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)


## Introduction

The priority queue library consists of two modules:

1. `lib.priorityqueue`: This module contains the implementation of 
    the `PrioQueue` class, which represents the priority queue. 
    It allows you to add new tasks with associated priorities and retrieve 
    them in the order based on their priority and reception time.

2. `test.test_priorityqueue`: This module contains unit tests for the 
    `lib.priorityqueue` module. It ensures the correctness of the 
    priority queue implementation by testing various scenarios and expected outcomes.


## Installation

To use the priority queue library in your project, you can simply copy the `prio-queue` 
directory to your project's directory. For linux users, if you need to you can add 
the package path to your environmental variables like:

         export PYTHONPATH=$PYTHONPATH:/your/path/to/prio-queue/


## Usage

To use the priority queue library, follow these steps:

- Import the `PrioQueue` class from the `lib.priorityqueue` module:
        
        from lib.priorityqueue import PrioQueue


- Create an instance of the PrioQueue class:

        queue = PrioQueue()


- Add new tasks to the queue using the enqueue method, 
    providing the command and priority level as arguments: 
        
        queue.enqueue("Buy John a Coffee", 1)
        queue.enqueue("Write Sarah a letter", 5)


-Retrieve the tasks from the queue in the desired order. 
    You can pring the calss instance directly. It uses the str() function 
    to obtain a string representation of the queue:

        print(queue)



## Examples
- Here are some examples demonstrating the usage of the priority queue library:
```
from lib.priorityqueue import PrioQueue

# Create a priority queue
queue = PrioQueue()

# Add new tasks
queue.enqueue("Buy John a Coffee", 1)
queue.enqueue("Write Sarah a letter", 5)
queue.enqueue("Walk the dog", 5)
queue.enqueue("Go shopping", 0)

# Print the queue
print(queue)

Output:

Order: 1 - Task: Write Sarah a letter
Order: 2 - Task: Walk the dog
Order: 3 - Task: Buy John a Coffee
Order: 4 - Task: Go shopping


===============================

# Process the tasks in the priority queue
queue.process_tasks()

Expected output:

Processing command: Write Sarah a letter (Priority: 5)
Processing command: Walk the dog (Priority: 5)
Processing command: Buy John a Coffee (Priority: 1)
Processing command: Go shopping (Priority: 0)

```




## Testing
- The priority queue library includes unit tests to ensure its correctness. 
    You can run the tests by executing the priorityqueue_test.py module:

        >>> cd prio-queue
        >>> test/priorityqueue_test.py


## Contributing
- Contributions to the priority queue library are welcome! 
    If you find any issues or have suggestions for improvements, 
    please feel free to open an issue or submit a pull request. 
    Contributions should follow the existing coding style and 
    include appropriate tests.



## License
- The priority queue library is released under the MIT License. 
    See the `LICENSE` file for more information.
