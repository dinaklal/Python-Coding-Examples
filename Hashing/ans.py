n = int(input())
has= {}
for i in range(n):
    has.update(dict(x.split() for x in input().splitlines()))
m = int(input())
for i in range(m):
    print(has[input()])