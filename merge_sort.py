## merge_sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left_a, right_a):
    merged = []

    Lcount = len(left_a)
    l_index = 0
    Rcount = len(right_a)
    r_index = 0

    while l_index < Lcount and r_index < Rcount:
        if left_a[l_index] <= right_a[r_index]:
            merged.append(left_a[l_index])
            l_index += 1
        else:
            merged.append(right_a[r_index])
            r_index  += 1
            
    while l_index < Lcount:
         merged.append(left_a[l_index])
         l_index += 1
            
    while r_index < Rcount:
          merged.append(right_a[r_index])
          r_index  += 1
        
    
    return merged


