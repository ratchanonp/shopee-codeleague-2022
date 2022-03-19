c = int(input()) 
d = []
x = []
count = 0
for i in range(c) :
    c_point = int(input())
    d.append(input().split())
    d[i] = ''.join(d[i])
for e in d :
    for i in range(len(e)//2) :
        if e.find(e[i],i+1) - e.find(e[i]) == 3 :
            count += 1
    x.append(count)
    count = 0
for i in range(len(x)):
    if x[i] >= c_point :
        print('no')
    else :
        print('yes')