from threading import *
from time import *

class MainThread:
    def __init__(self):
        print(current_thread().getName())
        for i in range(1,101):
            print(i)
        sleep(1)
        self.l=Lock()

    def EvenNumberThread(self):
        self.l.acquire()
        print(current_thread().getName())
        for i in range(1,101):
            if (i%2)==0:
                print(i)
        self.l.release()

    def OddNumberThread(self):
        self.l.acquire()
        print(current_thread().getName())
        for i in range(1,101):
            if (i%2)!=0:
                print(i)
        self.l.release()

obj=MainThread()
te = Thread(target=obj.EvenNumberThread())
te.start()

to = Thread(target=obj.OddNumberThread())
to.start()
