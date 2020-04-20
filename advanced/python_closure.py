import sys_logging


# Python program to illustrate
# nested functions
def outer_function(text):
    def inner_function():
        sys_logging.info(f'text = {text}')

    return inner_function


# A Closure is a function object that remember values in enclosing scopes even if they are not present in memory
if __name__ == '__main__':
    my_function = outer_function('Hey!')
    my_function()
