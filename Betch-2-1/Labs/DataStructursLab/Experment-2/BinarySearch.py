def BS(arr,key):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if key==arr[mid]:
            return f"element found at {mid+1}"
        elif key>mid:
            low=mid+1
        else:
            high=mid-1
    else:
        return "element not found"
arr=list(map(int,(input("enter elements:").split())))
key=int(input("enter key:"))
print(BS(arr,key))
