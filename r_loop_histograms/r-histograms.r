library(ggplot2)

df <- read.csv('pollen_sites.csv')
#summary(df)

# lapply(df, class)
# lapply(i, hist) 
# for(i in names(df)){
#   lapply(i, hist) 
#   #print i
#   hist(i, breaks=25)
# }
# value = 'pr1000mbldgbulkland'
# ggplot(df,aes(x = value)) + facet_wrap(~variable,scales = "free_x") + 
# geom_histogram()


# for (name in colnames(df)){
#   the_data <- df[,name]
#   #// do the stuff here
#   qplot(the_data, data=df, geom="histogram") 
# }

# i = 1
# 
#dev.off()


# for (name in colnames(df)){
#   x = paste(c('histograms/',name,'.png'), collapse='')
#   print(x)
#   qplot(name, data=df, geom="histogram")
#   dev.copy(png,filename=x);
#   dev.off();
# }


# # dev.off()
#dev.off()
#png("histograms/plot.png")



qplot(pr1000mbldgbulkland, data=df, geom="histogram")
# 
# 
# 
# 
# qplot(pr1000mbldgbulkland, data=df, geom="histogram", binwidth = 10)
dev.copy(png,filename="histograms/plot3.png");
dev.off ();

