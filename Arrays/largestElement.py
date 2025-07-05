def findLargest(arr):
  max = arr[0]
  for i in arr:
    if i > max:
      max = i
    else:
      continue
  return max

findLargest([3,4,7,1,2,10,0,1])
  
