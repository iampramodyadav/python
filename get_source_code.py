import inspect
def my_function(x, y):
   return x + y
  
source_code = inspect.getsource(my_function)
print(source_code)
