# Check if array is sorted or not
# assume array is in ascending 

def isSorted(arr):
    flag = True
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            flag = False
        else:
            continue
    if flag:
        print("True")
    else:
        print("False")
