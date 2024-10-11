def firstandlastsame(zList):
    print("Given list: ", zList)

    if zList[0] == zList[-1]:
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]
print("result is:", firstandlastsame(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print("result is:", firstandlastsame(numbers_y))