import pandas as pd
import matplotlib.pyplot as plt
import sys
#create dataframe
df=pd.read_csv(sys.argv[1])

#plot scatter with first column as x values and second column as y values
plt.scatter(df['year'],df['all_minerals___value'],color='#dd12dd',label="all_minerals")

#specifying labels
plt.xlabel("Year")
plt.ylabel("Value")

#enable legend
plt.legend()
plt.show()