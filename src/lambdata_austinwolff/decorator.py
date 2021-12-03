"""A decorator executes code both before or after or both - when we
run some function"""

def my_decorator(my_func):
  def wrapper():
    print("This happens before the function")
    my_func()
    print("This happens after the function")
  return wrapper

def my_func():
  print("Stuff my function does")

extended_func = my_decorator(my_func)

extended_func()