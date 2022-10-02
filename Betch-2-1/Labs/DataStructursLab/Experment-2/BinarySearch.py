arr=[1,2,3,4,5]
key=10
low,high=0,len(arr)-1
while low<=high:
    mid=(low+high)//2
    if key==arr[mid]:
        print(mid+1)
        break
    elif key>mid:
        low=mid+1
    else:
        high=mid-1
else:
    print("element not found")
    
