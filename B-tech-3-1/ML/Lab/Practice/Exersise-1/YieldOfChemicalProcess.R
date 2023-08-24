D <- data.frame(x=c(0,25,50,75,100),
                y=c(14,38,54,76,95))

fit <- lm(y ~ x, data=D)
summary(fit)


predict(fit, newdata=data.frame(x=80), interval="confidence",
        level=0.95)
# predict(fit, newdata = data.frame(x = 80), interval = "confidence", level = 0.95): 
 #This line of code is predicting the value of the response variable (y) for a new value of the predictor variable (x = 80) based on the linear regression model stored in the fit object. Here's what each argument means:
# fit: The linear regression model you previously created using the lm function.
# newdata: A data frame containing the new data points for which you want to make predictions. In this case, you're predicting for x = 80.
# interval: Specifies that you want to calculate a confidence interval.
# level: The confidence level for the interval, which is set to 0.95 (indicating a 95% confidence interval).
