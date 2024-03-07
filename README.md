
markdown
Copy code
# PyThreadFuture

PyThreadFuture is a Python class designed to simplify asynchronous task execution using ThreadPoolExecutor. This README provides detailed information on its features, usage, and example scenarios.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
    - [Initialization](#initialization)
    - [Decorators](#decorators)
    - [Waiting for Results](#waiting-for-results)
    - [Shutting Down](#shutting-down)
5. [Example](#example)
6. [License](#license)

## Introduction

Asynchronous programming is crucial for handling concurrent tasks efficiently. PyThreadFuture simplifies this process by providing decorator methods to execute functions in separate threads, along with utilities to manage and gather results from multiple asynchronous tasks.

## Features

- **async_task_no_return**: Decorator for running a task asynchronously without its result.
- **async_task_return**: Decorator for running a task asynchronously and returning a Future object for retrieving the result later.
- **run_and_wait**: Method to wait for and retrieve results from multiple futures.
- **shutdown**: Method to shut down the ThreadPoolExecutor, ensuring resource cleanup.

## Installation

PyThreadFuture can be installed via pip:

```bash
pip install pythreadfuture
Usage
Initialization
Create an instance of PyThreadFuture:

python
Copy code
from pythreadfuture import PyThreadFuture

executor = PyThreadFuture()
Decorators
Use decorators to run functions asynchronously:

python
Copy code
@executor.async_null_result
def task1():
    # Task logic here
python
Copy code
@executor.async_data_handler
def task2():
    # Task logic here
Waiting for Results
Use run_and_wait to wait for multiple tasks to complete and gather their results:

python
Copy code
future1 = task1()
future2 = task2()
results = executor.run_and_wait([future1, future2])
print("Results:", results)
Shutting Down
Call shutdown when done to clean up resources:

python
Copy code
executor.shutdown()
Example
Below is an example demonstrating the usage of PyThreadFuture:

python
Copy code
from time import sleep
from pythreadfuture import PyThreadFuture

executor = PyThreadFuture()

@executor.async_null_result
def example_task1():
    sleep(5)
    print("Task 1 completed")

@executor.async_data_handler
def example_task2():
    sleep(3)
    return "Task 2 completed"

future1 = example_task1()
future2 = example_task2()
results = executor.run_and_wait([future1, future2])
print("Results:", results)

executor.shutdown()
License
This project is licensed under the MIT License. See the LICENSE file for details.

Copy code
This expanded README provides a comprehensive overview of PyThreadFuture, including installation instructions, detailed usage guidelines, an example scenario, and licensing information. It aims to assist users in understanding and effectively utilizing the provided functionality.
