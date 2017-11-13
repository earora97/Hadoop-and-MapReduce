import sys

def reducer():
    airports=0
    oldKey=None
    max_total=0
    for line in sys.stdin:
        value_data=line.strip().split(" ")
        if(len(value_data)!=2):
            continue
        thisKey, c = value_data
        if oldKey and oldKey!=thisKey:
            if(airports>max_total):
                max_region=oldKey
                max_total=airports
            airports=0
        oldKey=thisKey

        airports+=float(c)

    print max_region
reducer()
