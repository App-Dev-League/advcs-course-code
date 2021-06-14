# idk seemed like a good example for recursion 😅🙂

def subsets(num: int, n:int, subset=[]):
    if(num==n):
        print(subset)
    else:
        subsets(num+1,n,subset)
        subset.append(num+1)
        subsets(num+1,n,subset)
        subset.pop()

