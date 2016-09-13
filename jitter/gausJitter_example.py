import numpy as np
import pandas as pd

inCSV = '<path and filename to your csv file>.csv'
ouCSV = '<path and filename to the output csv file with jittered points>.csv'
inLatField = '<input_latitude_field>'
inLngField = '<input_longitude_field>'

mu = 0
sigma = 0.001

df = pd.read_csv(inCSV)

df['latitude'] = df[inLatField ] +  np.random.normal(mu, sigma, size=len(df))
df['longitude']= df[inLngField ] +  np.random.normal(mu, sigma, size=len(df))

df.to_csv(ouCSV,index=False)
