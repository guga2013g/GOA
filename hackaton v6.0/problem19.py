def manual_max(list):
    min = 0
    for i in list:
        if min < i:
            min = i
    print(min)
manual_max([2,213,32,3,23,43,12])