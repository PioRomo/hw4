
def double(func): 
    def inner():
        #prints greet -> try that again -> greet again
        func()
        print('Lets try that again!')
        func()
    return inner



    
