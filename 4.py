x, y, n = map(int, input().split())
kop = (x * 100 + y) * n
print(kop//100, "руб.", kop - kop // 100 * 100, "коп.")