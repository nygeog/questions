#Looping through columns to create histograms for each	
	
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