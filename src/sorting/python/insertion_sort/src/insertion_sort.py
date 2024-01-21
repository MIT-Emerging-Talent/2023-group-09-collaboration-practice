def insertionsort(li):
    """
    Sorts items in a list (li) and returns a sorted list(ascending order)
    
    """
    for i in range(1, len(li)):
        k = i
        while li[k-1]>li[k] and k>0:
            li[k],li[k-1] = li[k-1],li[k]
            k -= 1
    return li