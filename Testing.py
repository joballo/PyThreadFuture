from PyThreadFuture import PyThreadFuture
# Initilaize the PyThreadFuture at the top of the file
executor = PyThreadFuture()

from time import sleep

class TestingClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    @executor.async_null_result
    def class_test_function1(self):
        print(f"Class test_function1 async_null_result")
        sleep(10)  # Simulate a time-consuming operation
        self.a = 100

    @executor.async_null_result
    def class_test_function2(self):
        print(f"Class test_function2 async_null_result")
        sleep(1)  # Simulate a time-consuming operation
        self.b = 200

    @executor.async_data_handler
    def class_test_function3(self):
        print(f"Class test_function3 async_data_handler")
        sleep(15)  # Simulate a time-consuming operation
        return self.a

    @executor.async_data_handler
    def class_test_function4(self):
        print(f"Class test_function4 async_data_handler")
        sleep(2)  # Simulate a time-consuming operation
        return self.b
# Create an instance of the TestingClass
testingclass=TestingClass()
# Run instances methods with async_null_result decorators. 
testingclass.class_test_function1()
testingclass.class_test_function2()

# The main program continues immediately without waiting for test_function to complete.
print("Continuing after class method with async_null_result...")

instance_future1 = testingclass.class_test_function3()
instance_future2 = testingclass.class_test_function4()

# Wait for all submitted tasks to complete and get their results
results = executor.run_and_wait([instance_future1, instance_future2])
print(f"Class instance result:{results}")
# The main program continues immediately without waiting for test_function to complete.
print("Continuing after class methods...")
print() # Print empty


@executor.async_null_result
def test_function1(a,b):
    print(f"test_function1 async_data_handler")
    sleep(10)  # Simulate a time-consuming operation
    return a+b

@executor.async_null_result
def test_function2(a,b):
    print(f"test_function2 async_data_handler")
    sleep(1)  # Simulate a time-consuming operation
    return a+b

@executor.async_data_handler
def test_function3(a,b):
    print(f"test_function3 async_data_handler")
    sleep(15)  # Simulate a time-consuming operation
    return a+b

@executor.async_data_handler
def test_function4(a,b):
    print(f"test_function4 async_data_handler")
    sleep(4)  # Simulate a time-consuming operation
    return a+b

# Run functions with async_null_result decorators. 
test_function1(10, 10)
test_function2(20, 20)
print("Continuing after fuction call with async_null_result...")

# Submit tasks to the executor
future3 = test_function3(30, 30)
future4 = test_function4(40, 40)

# Wait for all submitted tasks to complete and get their results
results = executor.run_and_wait([future3, future4])
print(f"function result:{results}")

# This must be added to release resouces.
executor.shutdown()
