def weight_average(my_list=[]):
    if(my_list):
        sum = 0
        for i in my_list:
            a = 1
            for j in i:
                a *= j
            sum += a
        b = 0
        for i in my_list:
            for j in i:
                a = j
            b += j
        return sum/b
    return 0
