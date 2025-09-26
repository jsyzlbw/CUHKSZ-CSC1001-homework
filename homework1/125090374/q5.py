from typing import List
def largest_even(arr: List) ->int:
    flag = True
    for item in arr:
        if type(item) == int and item % 2 == 0 and type(item) != bool:
            if flag:
                largest = item
                flag = False
            elif item > largest:
                largest = item
    if flag:
        return None
    return largest

def largest_k_evens(arr:List, k: int) ->List:
    result = []
    for i in range(k):
        largest = largest_even(arr)
        if largest != None:
            result.append(largest)
            arr.remove(largest)
        else:
            return result
    return result
