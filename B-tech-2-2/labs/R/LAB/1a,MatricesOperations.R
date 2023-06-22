m1<-matrix(1:9, nrow=3, ncol=3)
m2<-matrix(11:19, nrow=3, ncol=3)

print(m1)
print(m2)
'output:
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
     [,1] [,2] [,3]
[1,]   11   14   17
[2,]   12   15   18
[3,]   13   16   19
'

#add
print(m1+m2)
'output:
    [,1] [,2] [,3]
[1,]   12   18   24
[2,]   14   20   26
[3,]   16   22   28
'

#subtract
print(m1-m2)
'output:
[,1] [,2] [,3]
[1,]  -10  -10  -10
[2,]  -10  -10  -10
[3,]  -10  -10  -10
'

#element multiplicarion:
print(m1*m2)
'output:
    [,1] [,2] [,3]
[1,]   11   56  119
[2,]   24   75  144
[3,]   39   96  171
'

#matrix mul:
print(m1%*%m2)
'output:
     [,1] [,2] [,3]
[1,]  150  186  222
[2,]  186  231  276
[3,]  222  276  330
'

#transpose:
print(t(m1))
'output:
    [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
[3,]    7    8    9
'

#det of matrix
print(det(m2))
#output: 0