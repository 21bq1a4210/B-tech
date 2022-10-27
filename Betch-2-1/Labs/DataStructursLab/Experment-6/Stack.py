from array import *
class Stack:
    def __init__(self):
        self.arr=[]
    def push(self,data):
        self.arr.append(data)
        #print(self.arr)
    def pop(self):
        print(self.arr.pop(0))
    def isEmpty(self):
        if len(self.arr)==0:
            print("Stack is empty")
            return True
        else:
            print("Stack is not empty")
            return False
    def printStack(self):
        for i in range(len(self.arr)):
            print(self.arr[i],end=" ")
        print()

if __name__=="__main__":
    st=Stack()
    
    st.push(10)
    st.push(20)
    st.push(30)
    
    st.isEmpty()
    st.printStack()
    
    print('pop:')
    st.pop()
    st.pop()
    st.pop()
    
    st.isEmpty()
