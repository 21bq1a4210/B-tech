v1<-c(1:5)
v2<-c(6:10)

print(v1)
print(v2)
'output:
[1] 1 2 3 4 5
[1]  6  7  8  9 10
'
#add
print(v1+v2)
#output: [1]  7  9 11 13 15

#sub:
print(v1-v2)
#output: [1] -5 -5 -5 -5 -5

#mul:
print(v1*v2)
#output: [1]  6 14 24 36 50

#exponentiation
print(v1^v2)
#output: [1]       1     128    6561  262144 9765625

#length:
print(length(v1))
#output:[1] 5

#vector sum:
print(sum(v1))
#output: [1] 15

#max,min
print(min(v1)) #1
print(max(v1)) #10

#sort:
print(sort(v1))
#output: [1] 1 2 3 4 5