x<-c("a",'b','c','d')
print(x)
#output: [1] "a" "b" "c" "d"

print(seq(5,13,by=0.5))
#output:  [1]  5.0  5.5  6.0  6.5  7.0  7.5  8.0  8.5  9.0  9.5 10.0 10.5 11.0 11.5 12.0
#[16] 12.5 13.0

v<-5:13
print(v)
#output: [1]  5  6  7  8  9 10 11 12 13

#ACCESSING VECTOR:
t<-c('sun','mon','tue','wed','thr','fri','sat')
u<-t[c(2,5,7)]
print(u)
#output: [1] "mon" "thr" "sat"

#ACCESSING VECTOR USING LOGICAL INDEXING:
u<-t[c(FALSE,TRUE,FALSE,TRUE,TRUE,FALSE,TRUE)]
print(u)
#output:  [1] "mon" "wed" "thr" "sat"

#ACCESSING VECTOR USING NEGATIVE INDEXING:
u<-t[c(-2,-5,-7)]
print(u)
#output:  [1] "sun" "tue" "wed" "fri"

#VECTOR OPERATIONS:
  #VECTOR ARITHEMEATIC:
v1<-c(3,5,6,2,1,7)
v2<-c(4,7,8,1,2,3)

print(v1+v2)   #ADD
#output:  [1]  7 12 14  3  3 10

print(v1-v2)  #SUB
#output:  [1] -1 -2 -2  1 -1  4

print(v1*v2)  #MUL
#output:  [1] 12 35 48  2  2 21

print(v1/v2)  #DIV
#output:  [1] 0.7500000 0.7142857 0.7500000 2.0000000 0.5000000 2.3333333

# print(v1%v2)  #MOD
# Error: unexpected input in "print(v1%v2)"

#VECTOR ELEMENTS SORTING:
print(sort(v1)) 
#output:  [1] 1 2 3 5 6 7

print(sort(v1,decreasing = TRUE)) #revers order
#output: [1] 7 6 5 3 2 1

#VECTOR CHARACTER SORTING:
print(sort(t))
#output:  [1] "fri" "mon" "sat" "sun" "thr" "tue" "wed"

print(sort(t,decreasing = TRUE)) #revers order
#output:  [1] "wed" "tue" "thr" "sun" "sat" "mon" "fri"