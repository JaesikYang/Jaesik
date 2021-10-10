import sys
n = int(sys.stdin.readline())

a = [2]
for i in range(2, n+1):
            c = 0
            for k in a:
                if i % k == 0:
                    break
                else:
                    c += 1
                
                if c == len(a):
                    a.append(i)