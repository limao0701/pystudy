
def yd(len=10):
    global a
    print "deep=",a
    a+=1
    while(len>0):
        len-=1
        for x in yd(len):
            yield (x,)
        yield len

a=0
list(yd())
