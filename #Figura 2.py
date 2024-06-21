#Figura 4
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = 'https://docs.google.com/spreadsheets/d/1CyciF8ejNo_sxqqbw4SNu3dSRlnU9JsHq0zpWhKJebM/export?format=csv'
df = pd.read_csv(url)

df = df[df["Colesterol"] > 100]

df = df[df["Colesterol"] <= 400]

df = df[df["Colesterol"] > 0]

df['Sexo'] = df['Sexo'].replace({0: 'Mujer', 1: 'Hombre'})

bins = list(range(30, 77, 10)) + [np.inf]
labels = [ '30-39', '40-49', '50-59', '60-69', '70+']
df["Edad_intervalo"] = pd.cut(df["Edad"], bins=bins, labels=labels, right=False)

fig, ax = plt.subplots(figsize=(10, 6))
df.groupby(["Sexo", "Edad_intervalo"])["Colesterol"].mean().unstack().plot.bar(ax=ax)

for tick in ax.get_xticklabels():
    tick.set_rotation(90)

handles, labels = ax.get_legend_handles_labels()
labels = [label.replace('Edad_intervalo', 'Edad') for label in labels]
ax.legend(handles, labels)

ax.set_xlabel("Sexo y Edad")
ax.set_ylabel("Colesterol(mg/dL)")
ax.set_title("Relación entre Colesterol, Sexo y Edad")

ax.set_ylim(100, 260 + 20)
ax.set_yticks(np.arange(100, 260 + 21, 20))

plt.show()