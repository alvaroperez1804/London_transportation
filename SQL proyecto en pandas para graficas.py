import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import os
os.chdir(r"C:\Users\Hp\Desktop\Proyectos Data Analyst\segundo proyecto")
df = pd.read_csv("tfl_journeys_final.csv")
df = df.dropna()
df.loc[df["journey_type"] == "Bus", "Precio"] = np.random.uniform(1.5,3, size=len(df[df["journey_type"] == "Bus"]))
df.loc[df["journey_type"] == "Underground & DLR", "Precio"] = np.random.uniform(2.5,6, size=len(df[df["journey_type"] == "Underground & DLR"]))
df.loc[df["journey_type"] == "Overground", "Precio"] = np.random.uniform(6,8, size=len(df[df["journey_type"] == "Overground"]))
df.loc[df["journey_type"] == "TfL Rail", "Precio"] = np.random.uniform(9,11, size=len(df[df["journey_type"] == "TfL Rail"]))
df.loc[df["journey_type"] == "Tram", "Precio"] = np.random.uniform(12,15, size=len(df[df["journey_type"] == "Tram"]))
df.loc[df["journey_type"] == "Emirates Airline", "Precio"] = np.random.uniform(25,35, size=len(df[df["journey_type"] == "Emirates Airline"]))
print("el df incluyendo a precio")
print(df)
plt.style.use("dark_background")
plt.grid(color="#444444", linestyle="--", linewidth=0.5)
plt.scatter(df["journeys_millions"],df["Precio"])
plt.grid(color="#444444", linestyle="--", linewidth=0.5)
plt.xlabel("journeys_millions")
plt.ylabel("Price")
plt.title("Relacion entre numero de viajes y el precio")
plt.show
df_numerico = df.select_dtypes(include=['number'])  # Solo deja columnas numéricas
print(df_numerico.corr())  # Ahora sí calcula la correlación
#print(df.head(5))
#voy a quitar los valores nulos
df = df.dropna(subset=['journeys_millions'])
df_populares = df.groupby("journey_type")["journeys_millions"].sum().sort_values(ascending = False)
#esto me arroja una serie, debo hacer que me de un datafram que tenga dos columnas, la de journey_type y la de total
#debo crear un datafram usando reset_index
df_populares = df_populares.reset_index()
df_populares.columns = ["JOURNEY_TYPE","TOTAL_JOURNEYS_MILLIONS"]
print(df_populares)
plt.style.use("dark_background")
plt.grid(color="#444444", linestyle="--", linewidth=0.5)
plt.figure(figsize = (10,6))
plt.bar(df_populares["JOURNEY_TYPE"],df_populares["TOTAL_JOURNEYS_MILLIONS"])
plt.xlabel("JOURNEY_TYPE")
plt.ylabel("TOTAL_JOURNEYS_MILLIONS")
plt.title("Los journey_type mas populares")
plt.show()

#cuales fueron los 5 meses y los años donde el medio de transporte Emirates airlane fue mas popular
df_emiratos = df[df["journey_type"] == "Emirates Airline"]
df_emiratos = df_emiratos.dropna(subset=['journeys_millions'])
#print(df_emiratos)

df_emiratespopulares = df_emiratos.groupby(["month","year"])["journeys_millions"].sum().reset_index()
#print(df_emiratespopulares)
#vamos a saber primero los meses que mas se vendio, despues miramos como a eso le ponemos en que año paso eso
df_emirates_populares_sorted = df_emiratespopulares.sort_values(by="journeys_millions", ascending=False)
#usamos sort_values() porque el resultado que me da son numeros entonces tengo que especificar por que numero 
#vamos a ordenar
df_grafica = df_emirates_populares_sorted.head(5)
print(df_emirates_populares_sorted.head(5))
df_grafica["month_year"] = df_grafica["month"].astype(str) + "-" + df_grafica["year"].astype(str)

plt.style.use("dark_background")
plt.grid(color="#444444", linestyle="--", linewidth=0.5)
plt.figure(figsize = (10,6))
plt.bar(df_grafica["month_year"],df_grafica["journeys_millions"])
plt.xlabel("Month-Year")
plt.ylabel("TOTAL_JOURNEYS_MILLIONS")
plt.title("Los mejores meses de Emirates Airlane")
plt.grid(color="#444444", linestyle="--", linewidth=0.5)
plt.show()



#tercer ejercicio
df_under = df[df["journey_type"] == "Underground & DLR"]
df_under = df_under.groupby(["journey_type","year"])["journeys_millions"].sum().reset_index()
df_less_populars = df_under.sort_values(by="journeys_millions", ascending=True)
print(df_less_populars.head(5))

plt.style.use("dark_background")
plt.grid(color="#444444", linestyle="--", linewidth=0.5)
plt.figure(figsize=(10,6))
plt.bar(df_less_populars["year"], df_less_populars["journeys_millions"])
plt.xlabel("years")
plt.ylabel("Journey_millions")
plt.title("Years with less popularity for Underground & DLR ")
plt.show()
