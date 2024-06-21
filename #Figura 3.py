#Figura 3
import pandas as pd
import matplotlib.pyplot as plt


url = 'https://docs.google.com/spreadsheets/d/1CyciF8ejNo_sxqqbw4SNu3dSRlnU9JsHq0zpWhKJebM/export?format=csv'
df = pd.read_csv(url)


# Filter data
df = df[(df['Colesterol'] != 0) & (df['Sexo'] == 1) & (df['Edad'] >= 60) & (df['Edad'] <= 69)]


# Create boxplot
plt.boxplot(df['Colesterol'])


# Add labels and title
plt.xlabel('Hombres entre 60 y 69 años')
plt.ylabel('Colesterol (mg/dL)')
plt.title('Diagrama de cajas de Colesterol en hombres entre 60 y 69 años')


# Show plot
plt.show()