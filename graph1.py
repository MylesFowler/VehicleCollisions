import pandas as pd
import numpy as np
import time
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
importy sys

input_file = sys.argv[1]
df = pd.read_csv(input_file)

df['Side'].replace('R',1, inplace=True)
df['Side'].replace('L',0, inplace=True)

fig4, a = plt.subplots(ncols=1,figsize=(15,4))
sns.lineplot(x='City',y='Difference',hue='Side', ci=None, data=df).set_title("Graph (Collisions Side and City)")

fig5, a = plt.subplots(ncols=1,figsize=(15,4))
sns.lineplot(x='Difference',y='Distance(mi)',hue='Side', ci=None, data=df).set_title("Graph (Time difference by distance)")

fig6, a = plt.subplots(ncols=1,figsize=(15,4))
sns.lineplot(x='Difference',y='Severity',hue='Side', ci=None, data=df).set_title("Graph (Time difference by severity)")

fig3, ax = plt.subplots(ncols=3,figsize=(15,4))
sns.barplot(x='City',y='Difference', data=df,ax=ax[0],hue='Astronomical_Twilight').set_title('Time_Diff (Astronomical_Twilight)')
sns.barplot(x='City',y='Difference', data=df, ax=ax[1],hue='Nautical_Twilight').set_title("Time_Diff (Nautical_Twilight)")
sns.barplot(x='City',y='Difference', data=df,ax=ax[2],hue='Civil_Twilight').set_title("Time_Diff (Civil_Twilight)")


fig2, axs = plt.subplots(ncols=3,figsize=(15,4))
sns.lineplot(x='Difference', y='Temperature(F)', data=df, ax=axs[0],hue='City',ci=None).set_title("Time_Diff (Temperature(F))")
sns.lineplot(x='Difference', y='Humidity(%)', data=df, ax=axs[1],hue='City',ci=None).set_title("Time_Diff (Humidity(%))")
sns.lineplot(x='Difference', y='Pressure(in)', data=df, ax=axs[2],hue='City',ci=None).set_title("Time_DIff (Pressure(in))")


fig2.savefig('Time_Difference (by climate)')
plt.close(fig2)


fig3.savefig('Time_Difference')
plt.close(fig3)

fig4.savefig('Side')
plt.close(fig4)

fig5.savefig('Distance')
plt.close(fig5)

fig6.savefig('Severity')
plt.close(fig6)

plt.show()
