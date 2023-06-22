
data<-c(10,20,30)
label<-c('a','b','c')
color<-c('red','blue','green')
#Creat a Pie Chart
pie(data,labels = label,col=color, main='PIE CHART')

#Creat a Bar Chart
barplot(data,names.arg=label,col=color,main="bar chart",xlab='Xaxis',ylab='Y-axis')

#Create Scatter plot
x<-c(1,2,3,4,5)
y<-c(5,4,3,2,1)
plot(x,y,main='scatter plot',xlab='Xaxis',ylab = 'Yaxis')

#Create Histogram
data<-rnorm(1000)
hist(data,main='histogram',xlab='Vlues',ylab='Freq')
