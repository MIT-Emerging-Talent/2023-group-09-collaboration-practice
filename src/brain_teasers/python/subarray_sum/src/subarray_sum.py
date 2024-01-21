def subarray_sum(array, start, end):
    """
    function that iterates through the subarray and calculates the sum of elements
    returns (ans) an interger (sum of sub array)
    """
    # get indexes of the start and end
    storeStartId = array.index(start)
    storeEndId = array.index(end)
    ans = 0
    # add the numbers 
    for i in range(start, end):
        if array[i] == start:
            continue
        else:
           ans += array[i]
    return ans