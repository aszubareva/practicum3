N = int(input())
C = int(input())
number = int(input())
page = (number-1) // (N*C) + 1
remain = (number-1) % (N*C) # порядковый номер на текущей странице
column = remain // N + 1
string = remain % N + 1
print("страница", page, "столбец", column, "строка", string)