def a_decorator(a_function):

    def wrapper():

        print("this gets done before a_function() is called.")

        a_function()

        print("this gets done after a_function() is called.")

    return wrapper


def an_actual_function():
    print("i am an_actual_function!")


an_actual_function = a_decorator(an_actual_function)

an_actual_function()
