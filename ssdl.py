import matplotlib.pyplot as plt
import random
from matplotlib.font_manager import FontProperties


def dfs(pos):
    if pos == n:
        return 1
    res = [1, 1, 1, 1]
    for i in range(n):
        if matrix[pos][i] == 1:
            if c[i] != -1:
                res[c[i]] = 0
    for i in range(4):
        if res[i] == 1:
            c[pos] = i
            tmp = dfs(pos + 1)
            if tmp == 1:
                return 1
    c[pos] = -1
    return 0


font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
n = 50
m = 250
bitmap = [[0 for i in range(m)] for j in range(m)]
matrix = [[0 for i in range(n)] for j in range(n)]
c = [-1 for i in range(n)]
x = []
y = []
clo = []
que = []
cap = []
bound = []
plt.xticks([])
plt.yticks([])
plt.title('四色定理地图染色', fontproperties=font_set)
for i in range(n):
    xk = random.randint(0, m - 1)
    yk = random.randint(0, m - 1)
    while bitmap[xk][yk] != 0:
        xk = random.randint(0, m - 1)
        yk = random.randint(0, m - 1)
    bitmap[xk][yk] = i + 1
    que.append([xk, yk])
    cap.append([xk, yk])
print('首都确定完毕，开始扩张。')
while len(que):
    k = random.randint(0, len(que) - 1)
    xk = que[k][0]
    yk = que[k][1]
    if xk - 1 >= 0:
        if bitmap[xk - 1][yk] == 0:
            bitmap[xk - 1][yk] = bitmap[xk][yk]
            que.append([xk - 1, yk])
            continue
    if xk + 1 < m:
        if bitmap[xk + 1][yk] == 0:
            bitmap[xk + 1][yk] = bitmap[xk][yk]
            que.append([xk + 1, yk])
            continue
    if yk - 1 >= 0:
        if bitmap[xk][yk - 1] == 0:
            bitmap[xk][yk - 1] = bitmap[xk][yk]
            que.append([xk, yk - 1])
            continue
    if yk + 1 < m:
        if bitmap[xk][yk + 1] == 0:
            bitmap[xk][yk + 1] = bitmap[xk][yk]
            que.append([xk, yk + 1])
            continue
    que.pop(k)
# for i in range(m):
#     print(bitmap[i])
print('地图板块确定完毕，开始染色。')
for i in range(m - 1):
    for j in range(m - 1):
        if bitmap[i][j] != bitmap[i + 1][j]:
            matrix[bitmap[i][j] - 1][bitmap[i + 1][j] - 1] = 1
            matrix[bitmap[i + 1][j] - 1][bitmap[i][j] - 1] = 1
            bound.append([i + 0.5, j])
        if bitmap[i][j] != bitmap[i][j + 1]:
            matrix[bitmap[i][j] - 1][bitmap[i][j + 1] - 1] = 1
            matrix[bitmap[i][j + 1] - 1][bitmap[i][j] - 1] = 1
            bound.append([i, j + 0.5])
dfs(0)
print('染色完毕，开始画图。')
for i in range(m):
    for j in range(m):
        x.append(i)
        y.append(j)
        if c[bitmap[i][j] - 1] == 0:
            clo.append('#ff0000')
        if c[bitmap[i][j] - 1] == 1:
            clo.append('#00ff00')
        if c[bitmap[i][j] - 1] == 2:
            clo.append('#0000ff')
        if c[bitmap[i][j] - 1] == 3:
            clo.append('#ffff00')
plt.scatter(x, y, marker='s', c=clo, s=1)
for i in range(len(bound)):
    plt.scatter(bound[i][0], bound[i][1], s=0.5, c='k')
for i in range(len(cap)):
    plt.scatter(cap[i][0], cap[i][1], c='k', s=10)
    plt.annotate(i + 1, xy=(cap[i][0], cap[i][1]), xytext=(cap[i][0] + 0.1, cap[i][1] + 0.1))
plt.show()
plt.close()
print("结束。")
