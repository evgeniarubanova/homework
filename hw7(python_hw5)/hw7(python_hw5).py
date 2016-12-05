file=open("file2920.txt","r", encoding="utf-8")
n=0
qw=0
for line in file:
    n += 1
    arr=line.split()
    qw += len(arr)
print(qw/n)
file.close()
