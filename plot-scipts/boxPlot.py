import pandas as pd
import matplotlib.pyplot as plt
import sys
#create dataframe from csv
df=pd.read_csv(sys.argv[1], header=None, names=['col1', 'col2'])
plotMap=[]

#create a list of lists where each list will have a corresponding box plot
plotMap.append(df['col1'].dropna().tolist())
plotMap.append(df['col2'].dropna().tolist())

#plotting
plt.boxplot(plotMap)

#specifying labels
plt.xticks([1,2],["BoxPlot1","BoxPlot2"])
plt.xlabel("x-label")
plt.ylabel("y-label")


plt.legend()
plt.show()