import pandas as pd
import matplotlib.pyplot as plt
nume="ionescu"
prenume="stefan alexandru"
x=len(nume)
y=len(prenume)

df = pd.read_csv('data.csv')
df_x = df.head(x)  #x=7
df_y= df[['Durata', 'Puls']].head(y) #y=15
df.plot()
df_x.plot()
df_y.plot()
plt.show()


