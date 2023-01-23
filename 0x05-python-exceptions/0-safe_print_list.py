#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            count += 1
        except IndexError:
            pass
        print()
        return count
=======
    printed = 0
    if(my_list):
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end='')
                printed += 1
            except IndexError:
                print()
                return(printed)
    print()
    return(printed)
>>>>>>> 98c49ddb7483a160befcd9f26b92ba37d4e5151a
