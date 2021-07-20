import math

def dig_sum(num : int):
    if(len(str(num))==1):
        return num
    else:
        div=len(str(num))-1
        return math.floor(num/10**div)+dig_sum(int(str(num)[1:]))
