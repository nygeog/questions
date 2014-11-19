library(ggplot2)

df <- read.csv('pollen_sites.csv')

for (name in colnames(df)){
  x = paste(c('histograms/',name,'.png'), collapse='')
  print(x)
  qplot(name, data=df, geom="histogram")
  dev.copy(png,filename=x);
  #graphics.off();
  dev.off();
}
