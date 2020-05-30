class Stack():
  def __init__(self,list):
        self.list=list

  def push(self,value):
      self.list.append(value)

  def pop(self):
      return self.list.pop()

  def printstack(self):
       print(self.list)

a=Stack([1,2,3])
a.push(1)
a.push(2)
a.pop()
a.printstack()
