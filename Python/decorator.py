# decorator is function that takes function as input then modify it 
# this kind of functions is used to make changes to another functions 
# that is used to authenticate users and check if they has avalid login in the site 
# the syntatic suger is @decoreator name 
# this is more clean and readable and also easy to maintain 
# # @my_decorator 
# (Without @, you’d need to nest function calls → ugly and confusing).
# def say_hello():
#     print("Hello")
# another way to write it 
# Without @ → you decorate “after” the function.
# With @ → you decorate “at definition time” (right where you declare it).
# how python sees decorator 
# Python first creates say_hello as usual.
# → At this point, it’s just the plain function that prints "Hello".
# Then Python sees @my_decorator.
# It calls my_decorator(say_hello).
# That returns the wrapper function.
# Python reassigns the name:



def announce (f) : 
    def wrapper():
        print ("About to run ")
        f()
        print("Done running ") 
    return wrapper

@announce 
def say_hello() : 
    print ("Hello world")


def decor():
    def wrpper():
        print("")