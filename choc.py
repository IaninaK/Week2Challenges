m = int(input())
n = int(input())
k = int(input())
choc = m * n
if k % n == 0 and k < choc or k % m == 0 and k < choc:
    print("YES")
else:
    print("NO")
