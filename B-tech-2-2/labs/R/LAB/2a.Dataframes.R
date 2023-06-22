df<-data.frame(
  name=c('a','b','c','d','e'),
  age=c(12,23,34,45,56),
  city=c('q','w','e','r','t'),
  sal=c(1000,2000,3000,4000,5000)
)

print(df)
'output:
   name age city  sal
1    a  12    q 1000
2    b  23    w 2000
3    c  34    e 3000
4    d  45    r 4000
5    e  56    t 5000
'
#specific column:
print(df$name)
#output: [1] "a" "b" "c" "d" "e"

#1st 2 rows:
print(df[1:2,]) #',' imp bigglu
'output:
name age city  sal
1    a  12    q 1000
2    b  23    w 2000

3rd and5th row with 2nd and 4th column:'
print(df[c(3,5),c(2,4)])
'output:
  age  sal
3  34 3000
5  56 5000
'