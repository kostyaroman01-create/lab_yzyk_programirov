n, a = map(int, input().split())

count = 0

current = a

while count < n:
    if current % 2 != 0 and current % 3 != 0 and current % 5 != 0 and current % 7 != 0:
        print(current, end=" ")
        count += 1

    current += 1
