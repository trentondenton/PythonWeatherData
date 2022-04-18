#Name: Trenton Denton
#Date: 04/09/2021
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
plt.scatter(df1.index.values,df1['Humidity']); plt.suptitle('Humidity')
plt.show()
