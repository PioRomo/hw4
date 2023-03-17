
def double(func): 
    def inner():
        #prints greet -> try that again -> greet again
        func()
        print("Let's try that again!")
        func()
    return inner



    
