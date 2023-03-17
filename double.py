
def double(func): 
    def inner():
        #prints greet -> try that again -> greet again
        func()
        print('Lets try that again!')
        func()
    return inner


""""def greet():
    #print("Hello World")
    from test import greet

#sets double as the decorator and greet as the inner
decoratedFunc = double(greet)
decoratedFunc()
"""
    
