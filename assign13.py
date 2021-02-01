from threading import*
class Assignment:
    def even(self):
        i=0
        while(i<=101):
            if(i%2==0):
        print(i)
        else:
            continue
    def odd(self):
        i=0
        while(i<=101):
            if(i%2!==0):
         print(i)
        else:
            continue
a=Assignment()
p=Thread(target=even)

q=Thread(target=odd)

p.start()

q.start()