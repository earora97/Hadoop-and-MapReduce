import sys

def reducer():
    airports=0
    oldKey=None
    total_max=0
    for line in sys.stdin:
        value_data=line.strip().split(" ")
        if(len(value_data)!=2):
            continue
        thisKey, c = value_data
        if oldKey and oldKey!=thisKey:
            if(airports>total_max):
                max_country=thisKey
                total_max=airports
            airports=0
        oldKey=thisKey

        airports+=float(c)

    print max_country
reducer()
