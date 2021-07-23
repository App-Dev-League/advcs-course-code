def permute(n:int,num=1, per=[]):
    if(num==n+1):
        print(per)
    else:
        for i in range(n):
            if(not((i+1) in per)):
                break
        else:
            per.append(i+1)
            permute(n,num+1,per)
            per.pop()
