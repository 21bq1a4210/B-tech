#@title 8. Implement queue using array
class Q:
  def __init__(s,cap):
    s.cap=cap
    s.front=s.rare=0
    s.q=[0]*cap
  def enQ(s,data):
    if s.front==s.cap:
      print("Q is full")
    else:
      s.q[s.rare]+=data
      s.rare+=1
  def dQ(s):
    if s.front==s.rare:
      print("empty")
    else:
      x=s.q.pop(0)
      s.rare=-1
  def Dis(s):
    if s.front==s.rare:
      print("empty")
    else:
      for i in S.q:
        print(i,end='<=')