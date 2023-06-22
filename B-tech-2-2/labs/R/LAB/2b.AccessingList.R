l<-list(
  mat1<-matrix(1:9, nrow=3, ncol=3),
  srt='hi hello',
  num_vector=(1:10)
)

#Accessing ele by index
print(l[1])
'output:
[[1]]
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
'
print(l[2])
'output:
$srt
[1] "hi hello
'


#Accessing ele by name
print(l$srt)
#output: [1] "hi hello"

print(l$num_vector)
#output: 1]  1  2  3  4  5  6  7  8  9 10