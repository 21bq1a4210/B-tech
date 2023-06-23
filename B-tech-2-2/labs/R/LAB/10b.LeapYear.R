y<-as.numeric(readline(prompt = "enter a year:"))
if((y %% 4==0 && y%%100!=0)|| y%%400==0){
  print('yes')
}else{
  print('no')
}