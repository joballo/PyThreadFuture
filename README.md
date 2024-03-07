# PyThreadFuture

PyThreadFuture is a Python class that simplifies running tasks asynchronously using a ThreadPoolExecutor. It offers two decorator methods for executing functions in separate threads, along with methods for waiting for and retrieving results from multiple futures.

## Features

- **async_task_no_return**: Decorator for running a task asynchronously without its result.
- **async_task_return**: Decorator for running a task asynchronously and returning a Future object for retrieving the result later.
- **run_and_wait**: Method to wait for and retrieve results from multiple futures.
- **shutdown**: Method to shut down the ThreadPoolExecutor, ensuring resource cleanup.

# PyThreadFuture Testing code

- **Initialization**
import and Initialize the PyThreadFuture executor at the top of your file:

```python
from PyThreadFuture import PyThreadFuture
executor = PyThreadFuture()
```

- **example non blocking**
```python
testingclass.class_test_function1()
testingclass.class_test_function2()
```

```python
test_function1(10, 10)
test_function2(20, 20)
```

These methods or functions are invoked without awaiting their completion, as they do not return any values. They are particularly useful when there's a need to modify the internal state without needing to wait for a result.

- **example blocking**
```python
instance_future1 = testingclass.class_test_function3()
instance_future2 = testingclass.class_test_function4()

# Wait for all submitted tasks to complete and get their results
results = executor.run_and_wait([instance_future1, instance_future2])
print(f"Class instance result:{results}")
```

```python
# Submit tasks to the executor
future3 = test_function3(30, 30)
future4 = test_function4(40, 40)

# Wait for all submitted tasks to complete and get their results
results = executor.run_and_wait([future3, future4])
print(f"function result:{results}")
```

These methods or functions will wait for the results to be returned before proceeding. This code will block the execution of the remaining code until the tasks are completed.

## License
This project is provided under the MIT License, allowing users to freely use, modify, and distribute the code. See the LICENSE file for detailed licensing terms.

Copy code: This markdown file serves as a concise guide for users interested in utilizing the PyThreadFuture class for asynchronous task execution. It provides comprehensive features, usage instructions, and an example for better comprehension. Additionally, it emphasizes that the code is freely available for use.
