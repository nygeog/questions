import pandas as pd
import glob
import csv

csv_dir = 'data/'

csv_1 = csv.reader(csv_dir+'census_2010_block_st36_005100.csv')
csv_2 = csv.reader(csv_dir+'census_2010_block_st36_005200.csv')

# df_1 = pd.read_csv(csv_dir+'census_2010_block_st36_005100.csv')
# df_2 = pd.read_csv(csv_dir+'census_2010_block_st36_005200.csv')

#df   = pd.concat([df_1, df_2])#, ignore_index=True)

#print csv_1

for row in csv_1:
	print row

#

# m_csv = glob.glob(csv_dir+"*.csv")

# for mcsv in m_csv:
# 	print mcsv
# 	pd.read_csv(mcsv)





# fout=open(csv_dir + "a_out.csv","a")
# # first file:
# for line in open(csv_dir + "census_2010_block_st36_005100.csv"):
#     fout.write(line)
# # now the rest: 

# m_csv = glob.glob(csv_dir+".csv")

# for mcsv in m_csv:
#     f = open(mcsv)
#     f.next() # skip the header
#     for line in f:
#          fout.write(line)
#     f.close() # not really needed
# fout.close()