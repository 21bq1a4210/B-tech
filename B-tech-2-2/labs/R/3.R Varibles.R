#Variable Assignment
'The values of the variables can be printed using print() or cat() function. 
The cat() function combines multiple items into a continuous print output.'
v.1=c(0,1,2,3)
v.2<-c('a','b')
c(TRUE,1)->v.3

print(v.1)

cat('v.1:',v.1,'\n')
cat('v.2:',v.2,'\n')
cat('v.3:',v.3,'\n')

'output:
[1] 0 1 2 3
v.1: 0 1 2 3 
v.2: a b 
v.3: 1 1'

#Data Type of a Variable:
'a variable itself is not declared of any data type, rather it gets the data type of the R - object assigned to it.
So R is called a dynamically typed language '

v<-'hello'
cat('the class of v is:',class(v),'\n')

v<-10.43
cat('the class of v is:',class(v),'\n')

v<-27L
cat('the class of v is:',class(v),'\n')

v<-list(c(1,2,3),c('a','b','c'))
cat('the class of v is:',class(v),'\n')

'output:
the class of v is: character 
the class of v is: numeric 
the class of v is: integer 
the class of v is: list 
'

#Finding Variables:
'To know all the variables currently available in the workspace we use the ls() function.'
#print(ls())
'output:
[1] "a"          "apple_size" "BMI"       
 [4] "data"       "f_apple"    "fact_data" 
 [7] "gender"     "height"     "input_data"
[10] "l1"         "l2"         "labels"    
[13] "lbl"        "m"          "myString"  
[16] "negu"       "nu"         "piepercent"
[19] "t"          "u"          "v"         
[22] "v.1"        "v.2"        "v.3"       
[25] "v1"         "v2"         "v3"        
[28] "vect"       "weight"     "weigth"    
[31] "x"  '

#Deleting Variables:
'Variables can be deleted by using the rm() function.'
rm(v)
print(v) #output:Error in print(v) : object 'v' not found
