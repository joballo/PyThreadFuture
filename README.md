# PyThreadFuture

PyThreadFuture is a Python class that simplifies running tasks asynchronously using a ThreadPoolExecutor. It offers two decorator methods for executing functions in separate threads, along with methods for waiting for and retrieving results from multiple futures.

## Features

- **async_task_no_return**: Decorator for running a task asynchronously without its result.
- **async_task_return**: Decorator for running a task asynchronously and returning a Future object for retrieving the result later.
- **run_and_wait**: Method to wait for and retrieve results from multiple futures.
- **shutdown**: Method to shut down the ThreadPoolExecutor, ensuring resource cleanup.

## Usage

1. **Initialization**: Create an instance of `PyThreadFuture`.
```python
executor = PyThreadFuture()
