list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list2 = [[1, 2], [3, 4], [5, 6, 7]]  

flattedList = []
def flatter(l):
    for sublist in l:
        if type(sublist) == list:
            flatter(sublist)
        else:
            flattedList.append(sublist)
    return flattedList

def reverser(l):
    l.reverse()
    for sublist in l:
        if type(sublist) == list:
            reverser(sublist)
    return l

print(flatter(list1))
print(reverser(list2))