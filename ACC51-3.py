
from collections import deque
n, m = map(int, input("Enter the range (N M): ").split())
result = []
for i in range(10):
    queue = deque([i])
    while queue:
        stepnum = queue.popleft()
        if stepnum > m:
            continue
        if stepnum >= n and stepnum <= m:
            result.append(stepnum)
        lastdigit = stepnum % 10
        if stepnum == 0 or stepnum > m:
            continue
        if lastdigit > 0:
            nextstepnum = stepnum * 10 + (last_digit - 1)
            if nextstepnum <= m:
                queue.append(nextstepnum)
        if lastdigit < 9:
            nextstepnum = stepnum * 10 + (lastdigit + 1)
            if nextstepnum <= m:
                queue.append(nextstepnum)
result = sorted(result)
print(" ".join(map(str, result)))
