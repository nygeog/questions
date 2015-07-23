library(ggplot2)

setwd("/Users/danielmsheehan/GitHub/questions/r_loop_histograms/histograms/")
df <- read.csv('pollen_sites.csv')
head(df)[1:5]
for (ii in 2:ncol(df)){
  png(filename=paste("plot",colnames(df)[ii], sep="_" ))
  #p<-qplot(name, data=df, geom="histogram")
  p<-ggplot(data=df, aes(x=df[, 1], y=df[,ii]))+geom_point()+
    xlab(paste(colnames(df)[1]))+ylab(paste(colnames(df)[ii]))
  print(p)

  dev.off() 
}
