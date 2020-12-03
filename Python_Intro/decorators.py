import functools

def my_decorators(func):
    @functools.wraps(func)
    def function_with_func():
        print('start Decorators')
        func()
        print('end Decorator')
    return function_with_func


@my_decorators
def who_am_i():
    print('The middle Person')

who_am_i()


def second_decorator(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_with_func(*args,**kwargs):
            print('Start')
            if number == 0:
                print('Service is not running')
            else:
                func(*args,**kwargs)
            print('End')
        return function_with_func
    return my_decorator

@second_decorator(0)
def number_function():
    print('number')

number_function()
