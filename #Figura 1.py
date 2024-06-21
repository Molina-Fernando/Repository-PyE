#FIGURA 1

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = 'https://docs.google.com/spreadsheets/d/1CyciF8ejNo_sxqqbw4SNu3dSRlnU9JsHq0zpWhKJebM/export?format=csv'
df = pd.read_csv(url)

df = df[df["Presion arterial en reposo"] > 0]

df = df[df["Presion arterial en reposo"] <= 180]

df['Sexo'] = df['Sexo'].replace({0: 'Mujer', 1: 'Hombre'})

bins = list(range(30, 77, 10)) + [np.inf]
labels = [ '30-39', '40-49', '50-59', '60-69', '70+']
df["Edad_intervalo"] = pd.cut(df["Edad"], bins=bins, labels=labels, right=False)

fig, ax = plt.subplots(figsize=(10, 6))
df.groupby(["Sexo", "Edad_intervalo"])["Presion arterial en reposo"].mean().unstack().plot.bar(ax=ax)

for tick in ax.get_xticklabels():
    tick.set_rotation(90)

handles, labels = ax.get_legend_handles_labels()
labels = [label.replace('Edad_quintil', 'Edad') for label in labels]
ax.legend(handles, labels)

ax.set_xlabel("Sexo y Edad")
ax.set_ylabel("Presion arterial media en reposo (mmHg)")
ax.set_title("Relación entre Presión arterial media en reposo, Sexo y Edad")
ax.set_ylim(70, 140 + 10)
ax.set_yticks(np.arange(70, 140 + 11, 10))

plt.show()