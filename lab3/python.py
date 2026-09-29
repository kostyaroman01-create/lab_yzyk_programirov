программа 1
name=input("ведите имя " )
name2=input("ведите имя " )
print(name, "and", name2,"was here")
программа 2
name=input().split()
name2=input().split()
chered=[name[0],name2[0],name[1],name2[1],name[2]]
print(*chered, sep=', ')
программа 3
name, clov= input().split()
name2, clov2 = input().split()
name3, clov3 = input().split()

clova=(len(name)*int(clov)+len(name2)*int(clov2)+len(name3)*int(clov3))

print(clova)

программа 4
name = input()

zvezda = len(name) + 4

print('*' * zvezda)
print('* ' + name + ' *')
print('* ' * 0 + '*' * zvezda)
программа 5
startH, startM, startS = map(int, input().split())

finH, finM, finS = map(int, input().split())

stseconds = startH * 3600 + startM * 60 + startS
finseconds = finH * 3600 + finM * 60 + finS

distant = finseconds - stseconds

print(distant)
программа 6
n = int(input())
if n == 1:
    print('pusk')
else:
    print(n - 1)
программа 7
a, b, c = map(int, input().split())

if a == 3 and b == 3 and c == 3:
    print('hole')
else:
    print(a + b + c)
программа 8
a, b, c = map(int, input().split())

if a == 3 and b == 3 and c == 3:
    print('hole')
else:
    print(a + b + c)
программа 9
a, b, c = map(int, input().split())

if a == 3 and b == 3 and c == 3:
    print('hole')
else:
    print(a + b + c)
программа 10
right = max(a, b)

if c < left:
    print(left - c)
elif c > right:
    print(c - right)
else:
    print(0)

n = int(input())
программа 11
n = int(input())

print(n, end=" ")

while n != 1:
    if n % 2 != 0:
        n = 3 * n + 1
    else:
        n = n // 2

    print(n, end=" ")



программа 12
n = int(input())

print(n, end=" ")

while n != 1:
    if n % 2 != 0:
        n = 3 * n + 1
    else:
        n = n // 2

    print(n, end=" ")



программа 13
position = 0

while True:
    name = input()

    position += 1

    if name == 'Petr':
        print(position)
        break
программа 14
n, a = map(int, input().split())

count = 0

current = a

while count < n:
    if current % 2 != 0 and current % 3 != 0 and current % 5 != 0 and current % 7 != 0:
        print(current, end=" ")
        count += 1

    current += 1

программа 15
a, b = map(int, input().split())

while b != 0:
    a, b = b, a % b

print(a)

