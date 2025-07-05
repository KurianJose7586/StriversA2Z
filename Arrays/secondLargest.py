def secondLargest(arr):
    max = 0
    sec_max = 0

    for i in arr:
        if i > sec_max:
            if i > max:
                temp = max
                max = i
                sec_max = temp
            else:
                sec_max = i
        else:
            continue
    return sec_max
