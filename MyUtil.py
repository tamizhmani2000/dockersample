import sys

print("Sample Util File")

i = 10
str1 = "Check for String"

print(id(i))

print(str1[0])

a=6
if a==2:
    print("even")
elif a>5:
    print (">5")
else:
    print ("Below 5")


x=21
k=21
i=1
j=1
while i<x:
    while j<=k:
        sys.stdout.write('*')
        j=j+1

    print('\n')

    sys.stdout.write(" "*i)
    i = i + 1
    j = i
    k=k-1

