x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
answer = ""
deltaX = abs(x1 - x2)
deltaY = abs(y1 - y2)
if deltaX % 2 == 0 and deltaY % 2 == 0:
    answer = "YES"
elif deltaX % 2 != 0 and deltaY % 2 != 0:
    answer = "YES"
else:
    answer = "NO"
print(answer)
