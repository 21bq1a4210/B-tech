D <- data.frame(t=c(10,20,30,40,50,60,70,80,90),
                y=c(420,365,285,220,176,117,69,34,5))

fit <- lm(y ~ t, data=D)
summary(fit)

qt(.975,7)
# The code qt(.975, 7) in R is used to calculate the critical t-value for a two-tailed t-distribution with 7 degrees of freedom, where you're interested in the upper tail (0.025 significance level for each tail).
# Just to note, the qt function is part of the base R package, and it's used for working with the t-distribution and t-values.

-5.31+c(-1,1)*qt(.975,7)*0.2558
# -5.31: This is a constant term you're subtracting.
# c(-1,1): This creates a vector with two elements, -1 and 1. You're multiplying the critical t-value by both -1 and 1, which essentially gives you the values for the lower and upper bounds of a confidence interval.
# qt(.975, 7): This calculates the critical t-value at the 97.5th percentile of the t-distribution with 7 degrees of freedom.
# 0.2558: This is a constant multiplier.