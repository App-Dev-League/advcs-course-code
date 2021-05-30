def permute(n:int,num=1, per=[]):
  if(num==n+1):
    print(per)
  else:
    for i in range(n):
      if((i+1) in per):
        continue
      else:
        per.append(i+1)
        permute(n,num+1,per)
        per.pop()
