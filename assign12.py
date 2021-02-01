from datetime import *

class event:
    def __init__(self,starttime,endtime,venue):
        self.starttime=starttime
        self.endtime=endtime
        self.venue=[]

class venue:
    def __init__(self,name,address):
        self.name=name
        self.address=address

class address:
    def __init__(self,street,city,state,country,pincode):
        self.street=street
        self.city=city
        self.state=state
        self.country=country
        self.pincode=pincode

a1=address('MG Road','Mumbai','Maharashtra','Country','400056')
v1=venue('marriage',a1)
e1=event(date(2019,6,8),date(2019,6,9),v1)

print(e1.starttime,e1.endtime,e1.venue)
print('hosur','mg road','tamilnadu','india','635109')
print('marriage')