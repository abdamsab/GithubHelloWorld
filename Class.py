Class MyClass:
  
  def __init__(self, x=0, y=0, flag=True):
    self.__a = x
    self.__b = y
    self.__flag = flag
    
  def multi(self):
    if(self.__flag):
      print('a x b : ', a * b)
