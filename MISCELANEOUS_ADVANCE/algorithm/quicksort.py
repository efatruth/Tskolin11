l = [5, 2, 6, 8, 4]
def partition(l, low, high):
    pivot = l[high]
    i = -1
    for j in range(len(l)-1):
        if l[j] <= pivot:
            i += 1
            tmp = l[j]
            l[j] = l[i]
            l[i] = tmp

        tmp = l[high]
        i[high] = l[i+1]
        l[i+1] = tmp
        return i + 1

def quickSort(l, low, high):
    if low < high:
        index = partition(l, low, high)
        quickSort(l, low, index -1)
        quickSort(l, index - 1, high)

lst = [5, 2, 7, 8, 4]
quickSort(lst, 0, len(l) -1)
print(lst)
