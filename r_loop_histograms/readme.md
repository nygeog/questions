#Looping through columns to create histograms for each	

##Latest R code
This code doesn't seem to work I get an error:

<strong>Error in dev.copy(png, filename = x) : cannot copy from the null device</strong> 

Not sure what is going on here. Is the dev.off() turning off before the file has a chance to copy? 


	library(ggplot2)

	df <- read.csv('pollen_sites.csv')

	for (name in colnames(df)){
	  x = paste(c('histograms/',name,'.png'), collapse='')
	  print(x)
	  qplot(name, data=df, geom="histogram")
	  dev.copy(png,filename=x);
	  dev.off();
	}







	
##Python	
	
	import matplotlib.pyplot as plt
	import pandas as pd

	df = pd.read_csv('pollen_sites.csv') #bringing the csv into a dataframe

	dfL = list(df.columns.values) #getting a list of dataframe columns

	for i in dfL:
		print i 

		thePlot = df[i]

		plt.hist(thePlot)
		plt.title("Histogram for "+i)
		plt.xlabel("Value")
		plt.ylabel("Frequency")
		#plt.show()
		plt.savefig('histograms/hist'+i+'.png')

Actually, when I look at these png's the histograms are really bizarre.


		
I would like to try to do it in R. I assume the hist plots have some default breaks or something, as trying to define all the histogram bins and such might get a little crazy. 
		
##R
		
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
	
	
	
##Steve's R code: 
The structure you want in R is technically a vector and not a list, for what it’s worth.  R’s type naming scheme is odd. 
 
Anyway, I’d try:
 
	for (name in colnames(df)) {
	  the_data <- df[,name]
	  // do the stuff here
	  hist(the_data, breaks=25)
	}
 
Though that’s going to generate each histogram in order, each new one replacing the old one.  So you might want to output it into a PDF, like:
 
	pdf(“path_to_my_file”)
	for (name in colnames(df)) {
	…
	}
	dev.off()
 
Does that make sense?
 
Steve