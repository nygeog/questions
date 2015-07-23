library(ggplot2)

df <- read.csv('pollen_sites.csv')

qplot(pr1000mbldgbulkland, data=df, geom="histogram")
dev.copy(png,filename="histograms/plot3.png");
dev.off ();

