a = float(input())
hours = a // 30
minutes = int((a - hours * 30) * 2)
print(int(hours), minutes)