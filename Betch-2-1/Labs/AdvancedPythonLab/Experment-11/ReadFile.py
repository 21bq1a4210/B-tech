filename=input('Enter a file name')
f=open(filename,'r')
lcount=wcount=ccount=0
for line in f:
    lcount+=1
    wcount+=len(line.split())
    for l in line:
        if(l!=' ' and l!='\n'):
            ccount+=1
print('No. of Lines=',lcount)
print('No. of Words=',wcount)
print('No. of Characters=',ccount)
f.close()