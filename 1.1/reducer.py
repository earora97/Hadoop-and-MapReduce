import sys

def reducer():
    airports=0
    oldKey=None

    for line in sys.stdin:
        value_data=line.strip().split(" ")
        if(len(value_data)!=2):
            continue
        thisKey, x = value_data
        if oldKey and oldKey!=thisKey:
            print "{0} {1}".format(oldKey, airports)
            airports=0
        oldKey=thisKey

        airports+=float(x)
reducer()
