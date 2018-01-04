import pandas as pd
import matplotlib.pyplot as plt
import sys
#create dataframe
df=pd.read_csv(sys.argv[1], header=None, names=['col1', 'col2'])

#plot scatter with first column as x values and second column as y values
plt.scatter(df['col1'],df['col2'],color='#dd12dd',label="scatter-label")

#specifying labels
plt.xlabel("x-label")
plt.ylabel("y-label")

#enable legend
plt.legend()
plt.show()