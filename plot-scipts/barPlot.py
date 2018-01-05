import pandas as pd
import matplotlib.pyplot as plt
import sys


#reading data frame from a csv file
df=pd.read_csv(sys.argv[1])

#plot bar plot with xticks which is position of bars as first argument and height of bars as second argument
plt.bar(df['year'],df['all_minerals___value'],color='green',label="all_minerals")

#specify labels on xticks
#plt.xticks([1,2,3,4,5],["BarPlot1","BarPlot2","BarPlot3","BarPlot4","BarPlot5"])
plt.xlabel("Year")
plt.ylabel("Value")

#enabling legend
plt.legend()
plt.show()