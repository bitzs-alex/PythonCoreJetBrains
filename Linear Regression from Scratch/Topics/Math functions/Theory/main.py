import math

#  You can experiment here, it won’t be checked
a, b, c = [int(input()) for _ in range(3)]
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)
