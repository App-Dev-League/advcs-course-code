arr=list(map(int,input().split()))
arr.sort()
a=arr[0]
b=arr[1]
c=arr[6]-a-b
print(str(a) + " " + str(b) + " " + str(c))
