import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

try:
    a = [2]

    if n == 1:
        print(-1)
    elif n == 2:
        print(2)
        print(2)
    else:
        for i in range(2, n+1):
            c = 0
            for k in a:
                if i % k == 0:
                    break
                else:
                    c += 1
                
                if c == len(a):
                    a.append(i)

    for k in a:
        if k >= m:
            t = k
            break

    j = 0

    for i in range(a.index(t), len(a)):
        j += a[i]

    if n == 1:
        None
    elif n == 2:
        None
    else:
        print(j)
        print(t)

except:
    print(-1)