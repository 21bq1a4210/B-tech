'An operator is a symbol that tells the compiler to perform specific mathematical or logical manipulations. 
R language is rich in built-in operators and provides following types of operators.
'
'Types of Operators::
*Arithmetic Operators
*Relational Operators
*Logical Operators
*Assignment Operators
*Miscellaneous Operators
'
#Arithmetic Operators:
'
1. +
2. -
3. *
4. /
5. %%
6. %/%
7. ^
'

v1<-c(2,2.3,5)
v2<-c(4,5,2.2)

#1.Adds two vectors(+):
print(v1+v2)  #output: [1] 6.0 7.3 7.2

#2.Subtracts second vector from the first(-):
print(v1-v2)  #output:  [1] -2.0 -2.7  2.8

#3.Multiplies both vectors(*):
print(v1*v2)  #output: [1] 8.0 11.5 11.0

#4.Divide the first vector with the second(/):
print(v1/v2)  #output:  [1] 0.500000 0.460000 2.272727

#5.Give the remainder of the first vector with the second(%%):
print(v1%%v2) #output:  [1] 2.0 2.3 0.6

#6.	The result of division of first vector with second (quotient) (%/%):
print(v1%/%v2)  #output: [1] 0 0 2

#7.The first vector raised to the exponent of second vector(^):
print(v1^v2)  #output:[1] 16.00000 64.36343 34.49324


#Relational Operators:
'
1. >
2. <
3. ==
4. <=
5. >=
6. !=
'
v1<-c(2,5.5,6,9)
v2<-c(8,2.5,14,9)

#1.>
'Checks if each element of the first vector is greater than the corresponding element of the second vector.'
print(v1>v2)  #output:  [1] FALSE  TRUE FALSE FALSE

#2.<
'Checks if each element of the first vector is less than the corresponding element of the second vector.'
print(v1<v2) #output: [1]  TRUE FALSE  TRUE FALSE

#3.==
'Checks if each element of the first vector is equal to the corresponding element of the second vector.'
print(v1==v2) #output: [1] FALSE FALSE FALSE  TRUE

#4. <=
'Checks if each element of the first vector is less than or equal to the corresponding element of the second vector.'
print(v1<=v2) #output:  [1]  TRUE FALSE  TRUE  TRUE

#5.>=
'Checks if each element of the first vector is greater than or equal to the corresponding element of the second vector.'
print(v1>=v2) #output: [1] FALSE  TRUE FALSE  TRUE

#!=
'Checks if each element of the first vector is unequal to the corresponding element of the second vector.'
print(v1!=v2) #output: TRUE  TRUE  TRUE FALSE

#Logical Operators:
'
1. &
2. |
3. !
4. &&
5. ||
'
v1<-c(3,0,TRUE,2+3i)
v2<-c(4.23,1,FALSE,2+5i)

#1.&
'It combines each element of the first vector with the corresponding element of the second vector and gives a output TRUE if both the elements are TRUE.'
print(v1&v2)  #output: [1]  [1]  TRUE FALSE FALSE  TRUE

#2.|
'It combines each element of the first vector with the corresponding element of the second vector and gives a output TRUE if one the elements is TRUE.'
print(v1|v2) #output: [1] TRUE TRUE TRUE TRUE

#3.!
'Takes each element of the vector and gives the opposite logical value.'
print(!v1) #output: [1] FALSE  TRUE FALSE FALSE
print(!v2) #output: [1] FALSE FALSE  TRUE FALSE

'The logical operator && and || considers only the first element of the vectors and give a vector of single element as output.'

#4.&&
'Called Logical AND operator. Takes first element of both the vectors and gives the TRUE only if both are TRUE.'
print(v1&&v2)
