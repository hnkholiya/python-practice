f1=open('file1.txt')
f2=open('file2.txt','w')
for i in f1:
    f2.write(i.upper())
f2=open('file2.txt','r')
print(f2.read())