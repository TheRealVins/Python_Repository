def merge_list(list1,list2):
    resultlist=[]
    for num in list1:
        if num % 2 != 0:
            resultlist.append(num)
        
    for num in list2:
        if num %2 == 0:
            resultlist.append(num)
    
    print("result list: ", resultlist)

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

merge_list(list1, list2)
