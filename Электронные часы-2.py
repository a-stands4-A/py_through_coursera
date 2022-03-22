a = int(input())

hh = a // 3600 % 24
mm = a // 60 % 60
if mm // 10 == 0:
    mm = '0' + str(mm)
ss = a % 3600 % 60
if ss // 10 == 0:
    ss = '0' + str(ss)

print(hh, mm, ss, sep=':')
