library(ISLR)
library(MASS)
data("Auto")
typeof(data)
head(Auto)

pairs(Auto)

Auto$name<-NULL
cor(Auto, method = c('pearson'))

Lm.fit<-lm(mpg~. , data=Auto)
summary(Lm.fit)

which.max(hatvalues(Lm.fit))


par(mfrow=c(2,2))
plot(Lm.fit)


lm.fit = lm(mpg ~ . + displacement:weight, data = Auto)

summary(Lm.fit)

lm.fit = lm(mpg ~ . - name + I((displacement)^2) + log(displacement), data = subset(Auto, select = -c(name)))
lm.fit = lm(mpg ~ . - name + I((displacement)^2) + log(displacement) + displacement:weight, data = subset(Auto, select = -c(name)))
summary(Lm.fit)

