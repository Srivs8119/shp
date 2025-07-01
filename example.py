a=[1,2,1,2,1,4,5,6,7,7,8,8,2,2,1]
target=8
for i in range(0,len(a)):
    if a[i]==target:
        print("TRUE")
        break
if a[i]!=target:
    print("FALSE")

#example 2
a=[1,2,1,2,1,4,5,6,7,7,8,8,2,2,1]
target=1
count=0
for i in range(0,len(a)):
    if a[i]==target:
        count+=1
print(count)    

# example 3

a=[1,2,1,2,1,4,5,6,7,7,8,8,2,2,1]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

#example 4
a=[1,2,1,2,1,4,5,6,7,73,8,8,2,2,1]
max=0
for i in range(0,len(a)):
    if max<a[i]:
        max=a[i]
print(max)