import sys

n = int(sys.stdin.readline())

if n == 1:
    None
else:
    a = [2]
    cnt = 0

    while True:
        cnt += 1
        for i in a:
            c = 0
            if cnt % i == 0:
                break
            else:
                c += 1
        if c == len(a):
            a.append(i)

        while True:
            if n % i == 0:
                print(i)
                n = n/i
            else:
                break

        if n == 1:
            break