import math
# math.acos() - в радианы, math.degrees() - в градусы
a = int(input())
b = int(input())
c = int(input())
cos1 = (a**2 - b**2 + c**2) / (2*a*c)
cos2 = (b**2 - a**2 + c**2) / (2*b*c)
cos3 = (b**2 - c**2 + a**2) / (2*a*b)
print(math.degrees(math.acos(cos2)))
print(math.degrees(math.acos(cos1)))
print(math.degrees(math.acos(cos3)))