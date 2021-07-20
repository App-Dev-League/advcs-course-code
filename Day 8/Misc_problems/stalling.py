n=int(input())
height=[int(i) for i in input().split()]
stall=[int(i) for i in input().split()]
height.sort(reverse=True)
ans=1
for i in range(n):
    multiply=0
    for j in range(n):
        if(height[i]<=stall[j]):
            multiply+=1
    ans*=(multiply-i)
print(ans)
