# Here we are goindg to see about the multi threading.
# Here Each task is divided into sub tasks and allocated to each thread
'''
Thread is a light weight process.
Now a days all the computer have the Multi cores and according to their operations the process is been allocated by the creating the threads
Here we are going to learn how to create a thread
'''
from time import sleep
from threading import *

class step1(Thread):
    def run(self):
        for i in range(5):
            print("hello World")
            sleep(1)# Here the waiting time for 'step1' is 1 second
class step2(Thread):
    def run(self): # Here the both the classes have the same method.
        for i in range(5):
            print("Hello World2")
            sleep(1)# Here the waiting time for 'step2' is 1 second

s1 = step1()
s2 = step2()
# Here we are calling a object instead of calling the run method we supposed to call the start function
# s1.run()
# s2.run()
s1.start()
sleep(0.2)# here we are adding the sleep to avoid collsion of the two threads.
s2.start() #Here it will creates two threads and execute both the program simultaneously.
# Here after the execution of two threads we need to print the End Statement 

s1.join()
s2.join()
print("Ends Here...")# here the end statement gets executed before the two sub thread completing its process by the Main thread()
# inorder to hold the execution of Main thread we need to add the joins func, Which holds the main thread for the joining of the two created threads. 
'''
Here all of our executions are been handeled by the main thread then the program's class will be executed in the Main Thread
For executing the program we are creating the threads using the threads package.
'''

# Here on executing the program simultaneously on large range it leads to the Collision.
# To avoid collision we are adding the time delay from the package called time
# Even if we add a sleep some times it leads to a collision. Inorder to avoid such collsion we are adding the sleep to the calling portion