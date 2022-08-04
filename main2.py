import pandas as pd
import matplotlib.pyplot as plt
import numpy


# Creamos el dataframe
df = pd.read_csv("data/historico 2009 - 2021.csv",sep=";",na_values="",encoding ="ISO-8859-1")

# df.head()

# #mostrar ciertas columnas

# escuelas = df[['Provincia','Canton']]
# print(escuelas.head());

# print("-----------------------------")

# #mostrar ciertas filas
# fila0 = df.iloc[0]
# print(fila0)

# print("-----------------------------")


# #filtrados
# data = df[df['Periodo'] == '2012-2013']

# print(data.head())

#datos calculados


# def totalEstudiantes(fila):
# 	return fila['Estudiantes_Masculino']+fila['Estudiantes_Femenino']

# df['total_estudiantes'] = df.apply(totalEstudiantes,axis=1)

# data2 = df[['Provincia','Canton','Estudiantes_Masculino','Estudiantes_Femenino','total_estudiantes']]


# print(data2.head())


#agrupacion

data = df.groupby('Periodo').agg({
	'Estudiantes_Masculino':'sum'
})

# datafiltrado = data[data['Estudiantes_Masculino']>2210727]

data.to_csv("data.csv")

data['Estudiantes_Masculino'].plot(kind='bar')

plt.show()

