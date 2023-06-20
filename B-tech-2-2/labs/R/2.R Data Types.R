v <- TRUE
print(class(v)) #"logical"

v<-23.5
print(class(v)) #"numeric"

v<-2L
print(class(v)) #"integer"

v<-2+5i
print(class(v)) #"complex"

v<-'R prg'
print(class(v)) #"character"

v<-charToRaw('Yo..')
print(class(v)) #"raw"



#VECTORS
vect<-c('a','b','c')
print(vect) #"a" "b" "c"
print(class(vect))  #"character"

v1<-c(1,2,TRUE)
print(class(v1))  #"numeric"


#LIST
l1<-list(c(2,3,4),21.3,cos)
print(l1)
'output:
[[1]]
[1] 2 3 4

[[2]]
[1] 21.3

[[3]]
function (x)  .Primitive("cos")'


#MATRICES
m=matrix(c(1,2,3,4),nrow=2,ncol=2,byrow = TRUE)
print(m)
'output:
[,1] [,2]
[1,]    1    2
[2,]    3    4
'

#ARRAYS
a <- array(c('green','yellow'),dim = c(3,3,2))
print(a)
'output:
, , 1

     [,1]     [,2]     [,3]    
[1,] "green"  "yellow" "green" 
[2,] "yellow" "green"  "yellow"
[3,] "green"  "yellow" "green" 

, , 2

     [,1]     [,2]     [,3]    
[1,] "yellow" "green"  "yellow"
[2,] "green"  "yellow" "green" 
[3,] "yellow" "green"  "yellow"
'

#FACTORS
apple_size<-c(1,2,3,3,2,1,4,3,2,1)
f_apple<-factor(apple_size)
print(f_apple)
'outPut:
1] 1 2 3 3 2 1 4 3 2 1
Levels: 1 2 3 4'
print(nlevels(f_apple))
'output:
4
'

#DATAFRAMES
BMI <- 	data.frame(
  gender = c("Male", "Male","Female"), 
  height = c(152, 171.5, 165), 
  weight = c(81,93, 78),
  Age = c(42,38,26)
)
print(BMI)
'OUTPUT:
gender height weight Age
1   Male  152.0     81  42
2   Male  171.5     93  38
3 Female  165.0     78  26
'