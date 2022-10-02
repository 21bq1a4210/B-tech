class LinearSearch:
  def __init__(self,l,k):
    self.arr=l
    self.key=k
  @staticmethod
  def _Searching(self):
    f=0
    for i in range(len(self.arr)):
      if self.key==self.arr[i]:
        f+=1
        break
    else:
      print("element is not found")
    if f:
      print(f"element is found at the location:{i+1}")
  def find(self):
    LinearSearch._Searching(self)

obj=LinearSearch(l=list(map(int,input("enter the input list:").split())),k=int(input("enter key element:")))
obj.find()
