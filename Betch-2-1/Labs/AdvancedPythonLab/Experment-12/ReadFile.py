from collections import OrderedDict
filename=input('Enter a file name:')
file = open(filename, errors="ignore")
alphabet_buckets={}
for word in file.read().split():
   if(word[0].isalpha()):
       temp=word.lower()
       if(temp[0] not in alphabet_buckets.keys()):
           alphabet_buckets[temp[0]]=[]
           alphabet_buckets[temp[0]].append(temp)
       else:
           alphabet_buckets[temp[0]].append(temp)
file.close()
alphabet_buckets = OrderedDict(sorted(alphabet_buckets.items()))
#print(alphabet_buckets)
for x,y in alphabet_buckets.items():
    y=list(set(y))
    y.sort()
    print(f"{x}-{y}")