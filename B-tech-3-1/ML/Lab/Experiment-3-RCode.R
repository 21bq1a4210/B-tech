
# EXPERIMENT -3 :: Multiple Linear Regression


# Using multiple linear regression perform the following tasks on the Autodata set.
# (a) Produce a scatter plot matrix which includes all of the variable sin the data set.
#       (b) Compute the matrix of correlations between the variables using the function cor() . 
#            You will need to exclude the name variable, cor() which is qualitative.
#       (c) Use the lm() function to perform a multiple linear regression with mpg as the response 
#            and all other variables except name as the predictors. Use the summary() function to  
#            print the results.
# Comment on the output, That is
# i. Is there a relationship between the predictors and the response?
# ii. Which predictors appear to have a statistically 
#      significant relationship to the response?
# iii. What does the coefficient for the year variable suggest?
# (d)	Use the plot() function to produce diagnostic plots of the linear regression fit. 
# Comment on any problems you see with the fit.
# Do the residual plots suggest any unusually large outliers? 
# Does the leverage plot identify any observations with unusually high leverage?
# (e)	Use the * and : symbols to fit linear regression models with interaction effects. Do   
# any interactions appear to be statistically significant?
# (f)	Try a few different transformations of the variables, such aslog(X),√ X, X 2 .  
# Comment on your findings

#This question involves the use of multiple linear regression on the Auto data set.

library(ISLR)
library(MASS)
data("Auto")
typeof(data)
head(Auto)



#Produce a scatterplot matrix which includes all of the variables in the data set.


pairs(Auto)



#Compute the matrix of correlations between the variables using the function cor(). You will need to exclude the name variable, cor()which is qualitative.
Auto$name<-NULL
cor(Auto,method = c("pearson"))



lm.fit<-lm(mpg~.,data=Auto)
summary(lm.fit)


which.max(hatvalues(lm.fit))
## 14 
## 14
par(mfrow = c(2,2))
plot(lm.fit)



#Use the plot() function to produce diagnostic plots of the linear regression fit.
#Comment on any problems you see with the fit.
lm.fit = lm(mpg ~.-name+displacement:weight, data = Auto)
summary(lm.fit)


#Use the * and : symbols to fit linear regression models with interaction effects.
#Do any interactions appear to be statistically significant?
lm.fit = lm(mpg ~.-name+I((displacement)^2)+log(displacement)+displacement:weight, data = Auto)
summary(lm.fit)


#Try a few different transformations of the variables, such as log(X),√X, X2. Comment on your findings.
lm.fit = lm(mpg ~.-name+I((displacement)^2)+log(displacement)+displacement:weight, data = Auto)
summary(lm.fit)
