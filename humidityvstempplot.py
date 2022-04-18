#Name: Trenton Denton
#Date: 04/09/2021
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv") #baseline data is period 1 (older)
df2 = pd.read_csv("formatdata2.csv") #data for period 2 (more recent)
ax.set_title('Temperature vs. Humidity')
ax.set_label('Time')

plt.figure(); df2.Fahrenheit.plot(label = 'period 2'); df2.Humidity.plot(label = 'period 2'); plt.legend(loc='best'); plt.suptitle('Temperature vs. Humidity')
#plt.show()
