import pandas as pd
import matplotlib.pyplot as plt
import sys
#create dataframe from csv
df=pd.read_csv(sys.argv[1])
df2=df[['fuels___coal___value','all_minerals___value']]
#plotMap=[]

#create a list of lists where each list will have a corresponding box plot
#plotMap.append(df['year'].dropna().tolist())
#plotMap.append(df['fuels___coal___value'].dropna().tolist())
#plotMap.append(df['fuels___lignite___value'].dropna().tolist())

df2.boxplot()
#plotting
#plt.boxplot(plotMap)
#plt.boxplot()
#specifying labels
#plt.xticks([1,2],["coal","lignite"])
#plt.xlabel("Minerals")
plt.ylabel("value")


plt.legend()
plt.show()