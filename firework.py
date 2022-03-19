n, m, d = map(int, input().split())
coins = 0
fire = []
for i in range(m):
    ai, bi, ti = map(int, input().split())
    fire.append([ti,ai,bi])
fire.sort()
astart = fire[0][1]
for i in range(m):
    coins += fire[i][2] - abs(fire[i][1]-astart)
    astart = fire[i][1]
print(coins)