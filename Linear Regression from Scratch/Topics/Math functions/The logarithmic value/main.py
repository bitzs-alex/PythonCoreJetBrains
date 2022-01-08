import math

number = int(input().strip())
base = int(input().strip())
log_value = 0

if base <= 0 or base == 1:
    log_value = math.log(number)
else:
    log_value = math.log(number, base)

print(round(log_value, 2))
