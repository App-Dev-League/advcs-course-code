data={}
q=int(input())
while(q>0):
    stuff=list(map(int,input().split()))
    query=stuff[0]
    if(query):
        if(stuff[1] in data.keys()):
            print(data[stuff[1]])
        else:
            print(0)
    else:
        data[stuff[1]]=stuff[2]
    q-=1
