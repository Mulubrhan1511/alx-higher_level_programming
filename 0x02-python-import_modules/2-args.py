#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} arguments:".format(len(sys.argv[1:])))
    j = 1
    for i in sys.argv[1:]:
        print("{}: {}".format(j, i))
        j += 1
