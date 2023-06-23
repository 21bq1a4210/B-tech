x<-c(1,2,3,4,5)
y<-c(6,7,8,9,10)
z<-c(1,3,5,7,9)

#correlation
print(cor(x,z)) #output :[1] 1

#Linear Regression
print(lm(y ~ x))
'output:
Call:
lm(formula = y ~ x)

Coefficients:
(Intercept)            x  
          5            1  
'

#multiple regression:
print(lm(y~x+z))
'output:
Call:
lm(formula = y ~ x + z)

Coefficients:
(Intercept)            x            z  
          5            1           NA  
'