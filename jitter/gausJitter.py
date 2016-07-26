import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('ggplot')
#%matplotlib inline  

data = {'lat': [42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0,
                42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0,
                42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0,
                42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0,
                42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0,
                42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0,
                42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0,
                42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0,
                42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0,
                42.0,   42.0,  42.0,  42.0,  42.0,  42.0,  42.0,  42.0],
        'lng': [-73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0,
                -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0,
                -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0,
                -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0,
                -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0,
                -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0,
                -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0,
                -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0,
                -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0,
                -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0, -73.0]}
df = pd.DataFrame(data, columns=['lat', 'lng']) 
#df.head(5)

def gausJitter(inNum):
    mu, sigma = inNum, 0.001 # mean and standard deviation #http://gis.stackexchange.com/questions/8650/how-to-measure-the-accuracy-of-latitude-and-longitude
    jitter = np.random.normal(mu, sigma)
    return jitter

df['x'] = df.lng.map(gausJitter)
df['y'] = df.lat.map(gausJitter)  

x1, y1 = df['lng'], df['lat']
x2, y2 = df['x']  , df['y']
#print x2, y2
plt.scatter(x2, y2, alpha=0.6)
plt.scatter(x1, y1, color='red') #alpha=0.009)
plt.axis((-72.99,-73.01,41.99,42.01))
#http://stackoverflow.com/questions/8671808/matplotlib-avoiding-overlapping-datapoints-in-a-scatter-dot-beeswarm-plot
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html
plt.show()