import sys
def mapper():
    x=1
    for line in sys.stdin:
        if x==1:
            x+=1
            continue
        value_data = line.strip().split(',')
        if(len(value_data)!=7):
            continue
        _id, _type, name, lat, lon, country, region = value_data
        print _type[1:-1], "1"
mapper()
