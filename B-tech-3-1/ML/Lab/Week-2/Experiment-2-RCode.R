#Experiment -2
''' Using simple linear regression perform the following tasks on the Autodata set.
(a)	Use the lm() function to perform a simple linear regression with mpg as the response and horsepower as the predictor. 
(b)	Use the summary() function to print the results. Comment on the output.
That is
   i. Is there a relationship between the predictor and the response?
  ii. How strong is the relationship between the predictor and the response?
  iii. Is the relationship between the predictor and the response positive or   
negative?
  iv. What is the predicted mpg associated with a horsepower of98? What are  
the associated 95% confidence and prediction intervals?
  (c)	Plot the response and the predictor. Use the abline() function to display the least squares regression line.
(d)	Use the plot() function to produce diagnostic plots of the least squares regression fit. Comment on any problems you see with the fit.
'''
library(ISLR)
library(MASS)
data("Auto")
typeof(data)
head(Auto)

### apply the lenear Regression model (lm)
lm.fit<-lm(mpg~horsepower,data=Auto)
summary(lm.fit)

## Predictions

predict(lm.fit,data.frame(horsepower=c(98)),interval="prediction")

predict(lm.fit,data.frame(horsepower=c(98)),interval="confidence")

#Plot the response and the predictor. Use the abline() function to display the least squares regression line.
attach(Auto)
plot(horsepower,mpg)
abline(lm.fit,lwd=5,col="blue")

which.max(hatvalues(lm.fit))
par(mfrow = c(2,2))
plot(lm.fit)

