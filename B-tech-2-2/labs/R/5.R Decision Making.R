#R - Decision making
'
1. if statement
2. if else statement
3. switch statement
'

#1,if statement:
'syntax:
if(boolean_expression) {
   // statement(s) will execute if the boolean expression is true.
}
'
x<-30L
if(is.integer(x)){
  print('x is an integer')
}

#2. if else statement

'syntax:
if(boolean_expression) {
  // statement(s) will execute if the boolean expression is true.
} else {
  // statement(s) will execute if the boolean expression is false.
}'

x <- c("what","is","truth")

if("Truth" %in% x) {
  print("Truth is found")
} else {
  print("Truth is not found")
}
'output:
[1] "Truth is not found"'
