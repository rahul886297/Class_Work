#Write a function to evaluate expression "res=i*10" for all
import time

nList=[123213, 234, 33223423, 2344444, 10000000]
n=1000
def testfn(n):
    for i in range(0,n):
        res=i*10

for n in nList:
    start_time=time.time()*1000 #recording timein milli second
    #execute function
    testfn(n)

    end_time=time.time()*1000
    diff=end_time-start_time

    print(f"exection time for n = {n} is \n {diff} milli sec")
    