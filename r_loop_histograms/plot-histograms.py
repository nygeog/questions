import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('pollen_sites.csv')

dfL = list(df.columns.values)

for i in dfL:
	print i

	thePlot = df[i]

	plt.hist(thePlot)
	plt.title("Histogram for "+i)
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	#plt.show()
	plt.savefig('histograms/hist'+i+'.png')