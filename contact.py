#! /usr/bin/python
import sys
import os
import cPickle as p
''' python contact for add, remove, list, find ... contacts '''
class contactInfo:
    def __init__(self, name, age, addr, tel, group='default'):
        self.name=name
        self.age=age
        self.addr=addr
        self.tel=tel
        self.group=group
    def setName(self, s):
        self.name=s
    def setAge(self, s):
        self.age=s
    def setAddr(self, s):
        self.addr=s
    def setTel(self, s):
        self.tel=s
    def setGroup(self, s):
        self.group=s
    def getName(self):
        return (self.name)
    def getAge(self):
        return (self.age)
    def getAddr(self):
        return (self.addr)
    def getTel(self):
        return (self.tel)
    def getGroup(self):
        return (self.group)
    def getInfo(self):
        print 'name:%s  aget:%d  addr:%s  tel:%s  group:%s' \
        %(self.name,self.age,self.addr,self.tel,self.group)

class dic:
    ''' welcome to contact dictionary'''
    contactDic = {}
    def __init__(self):
        print '%s' %self.__doc__
    def printDic(self):
        for name,contact in self.contactDic.items():
            contact.getInfo() 
    def add(self,c):
        self.contactDic[c.getName()] = c
    def delete(self,c):
        del self.contactDic[c]

def saveContact():
    f = file(cwd+"/info.ci","w")
    p.dump(d,f)
    f.close
def readContact():
    f = file(cwd+"/info.ci")
    return p.load(f)
d = dic()
cwd=os.getcwd()
c = contactInfo('liutao',30,'Shanghai Songjiang District', '123456789')
d = dic();
c1 = contactInfo('liutao1',31,'Shanghai Songjiang District', '0123456789')
d.add(c)
d.add(c1)
saveContact()
d = readContact();
print "welcome to contact dictionary, you can use such commands:add del print:"
def add():
    name = raw_input("name:")
    age = raw_input("age:")
    addr = raw_input("address:")
    tel = raw_input("telephone:")
    tmpc = contactInfo(name,int(age),addr,tel);
    d.add(tmpc)
def delete():
    name = raw_input("name:")
    d.delete(name)    
while True:
    s = raw_input(">")
    if s.__eq__("add"):
        add(); 
    elif s.__eq__("del"):
        delete();
    elif s.__eq__("print"):
        d.printDic()
    else:
        print 'unkonw command'
