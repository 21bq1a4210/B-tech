#INTRO TO LIST:
#creating a list:
l<-list(1,'apple',2,'bat',3,'cat')
print(l)
# output:
#   [[1]]
#   [1] 1
# 
#   [[2]]
#   [1] "apple"
# 
#   [[3]]
#   [1] 2
# 
#   [[4]]
#   [1] "bat"
# 
#   [[5]]
#   [1] 3
# 
#   [[6]]
#   [1] "cat"

#creating a list with multy datatypes:
l<-list(1,'a',TRUE,c(2,'b',FALSE))
print(l)
#output:
# [[1]]
# [1] 1
# 
# [[2]]
# [1] "a"
# 
# [[3]]
# [1] TRUE
# 
# [[4]]
# [1] "2"     "b"     "FALSE"

#NAMING LIST ELEMENTS:
#create a list which containds vector,mat and list:
l<-list(c(1,2,3),matrix(c(3,9,5,1,2,3),nrow = 2),list(1,2,3))
print(l)
#output:
# [[1]]
# [1] 1 2 3
# 
# [[2]]
# [,1] [,2] [,3]
# [1,]    3    5    2
# [2,]    9    1    3
# 
# [[3]]
# [[3]][[1]]
# [1] 1
# 
# [[3]][[2]]
# [1] 2
# 
# [[3]][[3]]
# [1] 3

#namming list elements:
names(l)<-c("vector","matrix","nested_list")
print(l)
#output:
# $vector
# [1] 1 2 3
# 
# $matrix
# [,1] [,2] [,3]
# [1,]    3    5    2
# [2,]    9    1    3
# 
# $nested_list
# $nested_list[[1]]
# [1] 1
# 
# $nested_list[[2]]
# [1] 2
# 
# $nested_list[[3]]
# [1] 3

#ACCESSING THE LIST ELEMENTS:
print(l[1])   #througtt indexing
#output: $vector
#[1] 1 2 3

print(l$matrix)   #trougth namming
#output:
# [,1] [,2] [,3]
# [1,]    3    5    2
# [2,]    9    1    3

#Updating list elements:
l=list(1,2)
l[4]=4
print(l)
#output:
# [[1]]
# [1] 1
# 
# [[2]]
# [1] 2
# 
# [[3]]
# NULL
# 
# [[4]]
# [1] 4

#Updating list elements:
l[1]<-NULL
print(l)
#output:
# [[1]]
# [1] 2
# 
# [[2]]
# NULL
# 
# [[3]]
# [1] 4

#MERGING IN LIST:
#merging 2 list:
l1<-list(1,2,3)
l2<-list(4,5,6)
merge.default(l2,l1)
#output:
#   X4 X5 X6 X1 X2 X3
#1  4  5  6  1  2  3