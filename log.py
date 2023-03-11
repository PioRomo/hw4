from datetime import datetime 

def timestamp(func): 
    def inner(): 
        print(datetime.now())
        func()
    return inner
