import time

#nList=[123213, 234, 33223423, 2344444, 10000000]
n=10000000
def testfn(n):
    for i in range(0,n):
        res=i*10

def wrapper(func,*args,**kwargs):
    def wrapped(*args,**kwargs):
        start_time=time.time()*1000 #recording timein milli second
        #execute function
        func(*args,**kwargs)

        end_time=time.time()*1000
        diff=end_time-start_time

        print(f"exection time for n = {n} is \n {diff} milli sec")
    # wrapped(*args,**kwargs    )/
    return (wrapped)
    

newWapperdfn =wrapper(testfn,n)

newWapperdfn(n)