j1 = int(input("Enter the Capacity of Jug-1 in Liters: "))
j2 = int(input("Enter the Capacity of Jug 2 in Liters: "))
g = int(input("Enter the Required water in Jug-1:"))
def apply_rule(ch, x, y):
    # Rule 1 : Fill jug 1
    if ch == 1:
      # empty sapce in jug 1 should be less then its capacity 
      if x<j1:
        return j1,y
      else:
          print("Rule cannot be applied")
          return x,y
    # Rule 2:Fill jug 2
    elif ch == 2:
      # empty sapce in jug 2 should be less then its capacity 
      if y<j2:
        return x ,j2
      else:
        print("Rule cannot be applier")
        return x,y
    # Rule 7:Transfer all water from jug 1 to jug 2
    if ch == 9:
      # jug 1 should not be empty and jug 1 + jug 2 should be more then its capacity of jug 2 
      if x > 0 and x+y <= j2:
        return 0,x+y
      else:
        print("Rule cannot be applier")
        return x,y
    
     # Rule 10:Transfer all water from jug 2 to jug 1
    if ch == 10:
      # jug 2 should not be empty and jug 1 + jug 2 should not be more then capacity of jug 1 
      if y > 0 and x+y <= j1:
        return x+y,0
      else:
        print("Rule cannot be applier")
        return x,y
    # Rule 7:Transfer some water from jug 1 to jug 2 until jug 2 is full
    if ch == 7:
      # jug 1 should not be empty and jug 1 + jug 2 should be more then or equal to capacity of jug 2 
      if x > 0 and x+y >= j2:
        return x-(j2-y), j2
      else:
        print("Rule cannot be applier")
        return x,y
    # Rule 8:Transfer some water from jug 2 to jug 1 until jug 1 is full
    if ch == 8:
      # jug 2 should not be empty and jug 1 + jug 2 should be more then or equal to capacity of jug 1 
      if y > 0 and x+y >= j1:
        return j1,y-(j1-x) #x-(j1-x), j1
      else:
        print("Rule cannot be applier")
        return x,y
    # Rule 5:empty jug 1
    if ch == 5:
      # check if jug 1 is not already empty  
      if x > 0:
        return 0,y
      else:
        print("Rule cannot be applier")
        return x,y
    # Rule 6:empty jug 2 
    if ch == 6:
      # check if jug 2 is not already empty  
      if y > 0:
        return x,0
      else:
        print("Rule cannot be applier")
        return x,y
    # invalid choice 
    else:
      print("INVALID CHOICE")
# intialize capacity of both jugs as 0
x = y = 0
print("================================STATUS===========================")
print("The Initial State is:", end = " ")
print(x, y)
while(True):
  if (x==g):#or (y==g):
    print('***************  GOAL ACHIEVED! ******************')
    break
  else:
    print("================================RULES==============================")
    print("Rule 1: Fill Jug-1")
    print("Rule 2: Fill Jug-2")
    print("Rule 3: Pour Some Water from Jug-1") # not used 
    print("Rule 4: Pour Some Water from Jug-2") # not used
    print("Rule 5: Empty Jug-1 ")
    print("Rule 6: Empty Jug-2 ")
    print("Rule 7: Transfer some water from Jug-1 to jug 2 until Jug-2  is full")
    print("Rule 8: Transfer some water from Jug-2 to jug 1 until Jug-1 is full")
    print("Rule 9: Transfer all water from Jug-1 to Jug-2")
    print("Rule 10: Transfer all water from Jug-2 to Jug-1")
    ch = int(input("Enter rule to apply: "))
    x, y = apply_rule(ch, x, y)
    print("================================STATUS===========================")
    print("After Applyting the Rule, then the Current State is:", end = " ")
    print(x, y)