import sys

a = []
for line in sys.stdin:
  a.append(int(line))

a.sort(lambda x, y: y - x)

for i in range(3):
  print a[i]
