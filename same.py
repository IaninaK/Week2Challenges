a = int(input())
b = int(input())
c = int(input())
same = 0
if a == b or b == c or a == c:
    same = 2
if a == b and b == c and c == a:
    same = 3
print(same)
