n = int(input())
cow = n % 10
if 5 <= n <= 20:
    extension = ""
else:
    if cow == 1:
        extension = 'a'
    elif 2 <= cow <= 4:
        extension = "y"
    elif cow == 0:
        extension = ""
print(n, "korov" + extension)
 