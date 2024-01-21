def selectionsort_v1(li):
    """
    Sorts items in a list (li) and returns a sorted list (li)(ascending order)
    """
    for i in range(len(li)):
        minid = i
        for j in range(i+1,len(li)):
            minid = j
        li[i],li[minid] = li[minid],li[i]
    return li
