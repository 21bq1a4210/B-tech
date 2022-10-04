class InsertionSort:
    def __init__(self,arr):
        self.arr=arr
        InsertionSort.sort(self)
        InsertionSort.display(self)
    @staticmethod
    def sort(self):
        for i in range(1,len(arr)):
            temp=self.arr[i]
            j = i-1
            while j>=0 and temp<self.arr[j] :
                self.arr[j+1]=self.arr[j]
                j-=1
            self.arr[j+1]=temp
    @staticmethod
    def display(self):
        print(self.arr)

arr=list(map(int,input("enter elements:").split()))
obj=InsertionSort(arr)
