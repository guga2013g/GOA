def manual_min(list):
    max = 0
    for i in list:
        if max < i:
            max = i
    print(max)
manual_min([213,720,2,20,30])