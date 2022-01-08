import math

number = int(input().strip())
radian = math.radians(number)
print(round(1 / math.tan(radian), 10))
