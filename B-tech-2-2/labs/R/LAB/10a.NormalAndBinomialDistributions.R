data<-c(1,2,3,4,5,6,7,8,9,10)

#normal distribution
normal_data<-rnorm(1000, mean=mean(data), sd=sd(data))
hist(normal_data,main='Normal distribution')

#Binomial:
binomi_data<-rbinom(1000,size=length(data),prob=0.5)
hist(binomial_data,main='binomial distribution')

print(mean(normal_data)) #output:[1] 5.329903
print(sd(normal_data)) #output: [1] 2.9995

print(mean(binomi_data)) #output:[1] 4.91
print(sd(binomi_data))  #output:[1] 1.620656
