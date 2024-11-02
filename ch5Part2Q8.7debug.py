def sub_lists(lst, size):
    listOfSubLists = []
    subListCount = len(lst) // size 
    if len(lst) % size != 0:
        subListCount +=1
        
    for i in range(subListCount):
        sublist = []
        g = i * size
        print(f'this is outer iteration #{i+1}')
        for j in range(g,(g+size)):
            print(f'this is inner iteration #{j+1}')
            num = lst[j]
            sublist.append(num)
            if j == len(lst) -1:
                break
        listOfSubLists.append(sublist)
        
    return listOfSubLists

bruh = sub_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
print(bruh)