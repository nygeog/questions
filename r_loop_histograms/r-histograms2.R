library(ggplot2)

df <- read.csv('pollen_sites.csv')

# for (name in colnames(df)){
#   x = paste(c('histograms/',name,'.png'), collapse='')
#   print(x)
#   png(filename=x)
#   qplot(name, data=df, geom="histogram")
#   dev.copy(png) #;
#   #graphics.off() #;
#   #dev.off() #;
#   dev.off() #;
# }


png(filename="histograms/plot50.png")
qplot(pr1000mbldgbulkland, data=df, geom="histogram")
dev.copy(png)
graphics.off()
#dev.off()

png(filename="histograms/plot51.png")
qplot(pr0500mbldgbulkland, data=df, geom="histogram")
dev.copy(png)
dev.off()
dev.off()