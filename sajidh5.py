#LARGEST OF NUMBERS_SAJIDH

a,s,r=map(int,input().split())

if a>s and a>r:
    print(a)
elif s>r:
    print(s)
else:
    print(r)
