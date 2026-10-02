# Binary Search

arr = [5,10,16,23,37,67,89]

search = 67
low = 0
high = len(arr)-1

while low<=high:
    mid = (low + high)//2

    if arr[mid] == search:
        print(" Successful Search! ")
        print("Element found at index: ",mid )
        break
    elif arr[mid] < search:
        low = mid+1

    else:
        high = mid-1
else:
    print("Element not Found! ")            
