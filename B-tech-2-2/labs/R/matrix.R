v1<-c(1,2,3,4)
print(matrix(v1, nrow = 2, ncol =2 ))
r_name<-c("r1","r2")
c_name<-c('c1','c2')
mat<-matrix(v1, nrow = 2, ncol = 2)
print(mat[1,2])


m1<-matrix(c(1,2,3,4,5,6), nrow = 2, ncol=  3)
m2<-matrix(c(6,5,4,3,2,1), nrow = 2, ncol = 3)
print(m1+m2)
print(m1-m2)
print(m1*m2)
