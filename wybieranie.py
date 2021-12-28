def find_min_index(lst,start):
    i = start
    for j in range(i+1, len(lst)):
        if lst[j]<lst[i]:
            i=j
    return i

def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = find_min_index(lst,i)
        lst[i],lst[min_idx] = lst[min_idx], lst[i]

arr=[12,34,51,22,33,11,99,23,43,87,221,34]

lst = arr(len(arr)-1)

def clone():
    print("I like potatoes")
 

find_min_index(lst)
