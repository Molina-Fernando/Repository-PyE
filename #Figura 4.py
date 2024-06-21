#Figura 4

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_excel('Dataset cardíacas.xlsx')

# Filter out rows with 0 cholesterol
data = data[data['Colesterol'] != 0]

# Create a new column for age quintiles
data['Edad_quintiles'] = pd.cut(data['Edad'], bins=[27, 39, 49, 59, 69, 200], labels=['30-39', '40-49', '50-59', '60-69', '70 o más'])

# Group the data by age quintiles and sex
grouped_data = data.groupby(['Edad_quintiles', 'Sexo'])

# Calculate the mean cholesterol for each group
mean_cholesterol = grouped_data['Colesterol'].mean()

# Create the bar chart
mean_cholesterol.unstack().plot(kind='bar')
plt.xlabel('Edad')
plt.ylabel('Colesterol medio (mg)')
plt.title('Relación entre Colesterol, Sexo y Edad.')
plt.show()

# Load the data
data = pd.read_excel('Dataset cardíacas.xlsx')

# Filter out rows with 0 cholesterol and greater than 400
data = data[(data['Colesterol'] != 0) & (data['Colesterol'] <= 400)]

# Create a new column for age quintiles
data['Edad_quintiles'] = pd.cut(data['Edad'], bins=[27, 39, 49, 59, 69, 200], labels=['30-39', '40-49', '50-59', '60-69', '70+'])

# Group the data by age quintiles and sex
grouped_data = data.groupby(['Edad_quintiles', 'Sexo'])

# Calculate the mean cholesterol for each group
mean_cholesterol = grouped_data['Colesterol'].mean()

# Create the bar chart
mean_cholesterol.unstack().plot(kind='bar')
plt.xlabel('Edad')
plt.ylabel('Colesterol medio (mg/dL)')
plt.title('Relación entre Colesterol, Sexo y Edad')
plt.legend(['Mujeres', 'Hombres'])
plt.ylim(100, 300)
plt.yticks(range(100, 300, 20))

plt.show()