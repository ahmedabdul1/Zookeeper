n = int(input())
r = int(input())
t = 0

while n > r:
    n = n / 2
    t += 1
    a = t * 12
print(a)
