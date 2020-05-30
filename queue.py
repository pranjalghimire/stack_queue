class Queue:
    def __init__(self,list):
        self.list=list

    def push(self,num):
        self.list.append(num)

    def pop(self):
        self.list.pop(0)

    def printqueue(self):
        print(self.list)

a=Queue([])
a.push(2)
a.push(3)
a.pop()
a.printqueue()
