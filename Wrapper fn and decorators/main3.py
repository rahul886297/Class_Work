import time

n=10000000

def wrapper_fn(func,*args,**kwargs):
    def wrapped(*args,**kwargs):
        start_time=time.time()*1000 #recording timein milli second
        #execute function
        func(*args,**kwargs)
        end_time=time.time()*1000
        diff=end_time-start_time

        print(f"exection time for n = {n} is \n {diff} milli sec")
    return (wrapped)

@wrapper_fn #decorator function
def testfn(n):
    for i in range(0,n):
        res=i*10

@wrapper_fn
def testfn2(n):
    for i in range(0,n):
        res=i*i
    print(res)
    
# newWapperdfn =wrapper(testfn,n)
# newWapperdfn(n)

testfn(n)