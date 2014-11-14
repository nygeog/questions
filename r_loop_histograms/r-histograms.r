library(ggplot2)

df <- read.csv('pollen_sites.csv')
summary(df)

lapply(df, class)
# lapply(i, hist) 
# for(i in names(df)){
#   lapply(i, hist) 
#   #print i
#   #hist(i, breaks=25)
# }

# ggplot(df,aes(x = value)) + 
#   facet_wrap(~variable,scales = "free_x") + 
#   geom_histogram()