startH, startM, startS = map(int, input().split())

finH, finM, finS = map(int, input().split())

stseconds = startH * 3600 + startM * 60 + startS
finseconds = finH * 3600 + finM * 60 + finS

distant = finseconds - stseconds

print(distant)