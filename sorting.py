#1. Binery Search:
def binery_search(x,val):
    l = 0
    h = len(x)-1
    m = 0
    while l <= h:
        m = (l+h)//2
        mid = x[m]
        if mid == val:
            return m
        if mid < val:
            l = m+1
        else:
            h = m-1
    return "Value not found"
x = [4,2,6,3,7,8,5]
x.sort()
print(binery_search(x,6))

#2. Merge sort:
def merge(x):
    if len(x)>1:
        mid = len(x)//2
        l = x[:mid]
        r = x[mid:]
        merge(l)
        merge(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                x[k] = l[i]
                i += 1
            else:
                x[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            x[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            x[k] = r[j]
            j += 1
            k += 1
x = [12,11,13,6,5,7]
print("Given array:", x)
merge(x)
print("Sorted array:", x)
   
#3.Quick sort:
def quicksort(x):
    if len(x) <= 1:
        return x
    else:
        p = x[0]
        left = [i for i in x[1:] if i<p]
        right = [i for i in x[1:] if i>=p]
        return quicksort(left) + [p] + quicksort(right)
x = [4,2,6,3,7,8,5]
print("Sorted array:", quicksort(x))

#4. Insertion sort:
def insertion(x):
    l = len(x)
    if l <= 1:
        return
    for i in range(1,l):
        n = x[i]
        j = i-1
        while j >= 0 and n < x[j]:
            x[j+1] = x[j]
            j = j-1
        x[j+1] = n
x = [12,9,14,15,13]
print("Original list:", x)
insertion(x)
print("Sorted list:", x)

#5. Sort list of strings:
list_str = ["edyoda", "class", "python", "data", "algorithm"]
list_str.sort()
print("Sorted:", list_str)