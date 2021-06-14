arr=list(map(int,input().split()))
#sorting the array makes our lives easier
arr.sort()
#since a is the least value, a will be first
a=arr[0]
#by the same logic as a, b will be second
b=arr[1]
#since a+b+c is the greates value, it will be last. We can use this to find c
c=arr[6]-a-b
print(str(a) + " " + str(b) + " " + str(c))
