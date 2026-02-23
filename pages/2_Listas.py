import streamlit as st
import pandas as pd

st.title("Método 2: Desde una Lista de Listas")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame partiendo de una **lista de listas** que represente el inventario de una tienda de tecnología.

1. Crea una lista de listas donde cada sub-lista contenga información de un producto: 
   `[Nombre del producto, Categoría, Precio, Cantidad en stock]`
   Agrega al menos 4 productos diferentes.
2. Crea un DataFrame llamado `df_inventario` a partir de esta lista y pásale el parámetro `columns=[]` definiendo cómo se llamarán tus columnas.
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

productos = [
    ["Teclado", "Periféricos", 25000, 50],       
    ["Monitor", "Monitores", 300000, 20],   
    ["Cable HDMI", "Accesorios", 35000, 100],   
    ["Disco Duro", "Almacenamiento", 309000, 15] 
]

df_inventario = pd.DataFrame(productos, columns=["Nombre del producto", "Categoria", "Precio", "Cantidad en stock"])

st.dataframe(df_inventario)
