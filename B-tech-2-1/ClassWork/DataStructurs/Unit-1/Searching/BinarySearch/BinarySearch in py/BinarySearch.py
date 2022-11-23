class BinarySearch:
    def __init__(self,arr,key):
        self.arr=arr
        self.key=key
        BinarySearch.search(self)
    @staticmethod
    def search(self):
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if key==arr[mid]:
                print(f"element found at {mid+1}")
                break
            elif key>mid:
                low=mid+1
            else:
                high=mid-1
        else:
            print("element not found")
arr=list(map(int,(input("enter elements:").split())))
key=int(input("enter key:"))
obj=BinarySearch(arr,key)
