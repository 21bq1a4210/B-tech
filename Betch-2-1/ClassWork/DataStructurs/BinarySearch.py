a=[20,3,17,19,25,35,9,42,16,27]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            print(f"iteration:{i+1} res:{a}")
print()
print(f"final sorted result:{a}")
