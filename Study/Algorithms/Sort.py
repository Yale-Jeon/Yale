import sys
sys.path.append(r"..\DataStructure")
from BinaryHeap import BinaryHeap

def SelectionSort(lst, reverse = False):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    if reverse == True:
        return lst[::-1]
    return lst

def MergeSort(lst, reverse = False):
    n = len(lst)
    if n == 1:
        return lst

    sub1 = []
    sub2 = []
    for i in range(n):
        if n/2 > i:
            sub1.append(lst[i])
        else:
            sub2.append(lst[i])

    sub1 = MergeSort(sub1)
    sub2 = MergeSort(sub2)

    idxCount1 = 0
    idxCount2 = 0
    nsub1 = len(sub1)
    nsub2 = len(sub2)
    for i in range(n):
        if idxCount1 == nsub1:
            lst[i] = sub2[idxCount2]
            idxCount2 += 1
        elif idxCount2 == nsub2:
            lst[i] = sub1[idxCount1]
            idxCount1 += 1
        elif sub1[idxCount1] > sub2[idxCount2]:
            lst[i] = sub2[idxCount2]
            idxCount2 += 1
        else:
            lst[i] = sub1[idxCount1]
            idxCount1 += 1
    if reverse == True:
        return lst[::-1]
    return lst

def HeapSort(lst, reverse = False):
    n = len(lst)
    Heap = BinaryHeap()
    ret = []
    for i in range(n):
        Heap.enqueue(lst[i], lst[i])
    for i in range(n):
        ret.append(Heap.dequeue())
    if reverse == True:
        return ret
    return ret[::-1]

def QuickSort(lst, pivot=0):
    n = len(lst)
    if n <= 1:
        return lst
    pivotValue = lst[pivot]
    less = []
    more = []
    for i in range(n):
        if i == pivot:
            continue
        elif lst[i] > pivotValue:
            more.append(lst[i])
        elif lst[i] <= pivotValue:
            less.append(lst[i])
    return QuickSort(less)+[pivotValue]+QuickSort(more)

def CountingSort(lst, reverse = False):
    n = len(lst)
    min = (-1)*float('INF')
    max = float('INF')
    for i in range(n):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]
    counting = range(max - min + 1)
    for i in range(len(counting)):
        counting[i] = 0
    for i in range(n):
        value = lst[i]
        counting[value - min] = counting[value - min] + 1
    cnt = 0
    for i in range(max - min + 1):
        for j in range(counting[i]):
            lst[cnt] = i + min
            cnt += 1
    if reverse == True:
        return lst[::-1]
    return lst