names = {}
n = int(input('Enter number of names:'))
for i in  range(n):
    names[i+1]=input('Enter a name:')
name = list(names.values())
pos = int(input('Enter position:'))
name.sort(key=lambda x:x[pos])
print(name)
