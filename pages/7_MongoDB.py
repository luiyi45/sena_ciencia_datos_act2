import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.title("Bases de Datos en la Nube: MongoDB")

st.markdown("""
### Ejercicio
MongoDB es una base de datos NoSQL muy popular que almacena la información de forma muy similar a JSON.

**Instrucciones:**
1. Imagina que tienes acceso a un clúster de MongoDB Atlas. Para este ejercicio no necesitas conectarte realmente a la base de datos a menos que tengas un clúster de prueba.
2. Basándote en el material de clase, escribe el **código necesario (comentado si no tienes conexión)** para conectarte usando `pymongo` y la clase `MongoClient`.
3. Supón que la base de datos se llama `Veterinaria` y la colección se llama `mascotas`.
4. El código debe incluir cómo extraer los documentos y convertirlos en el DataFrame `df_mongo`.
""")

st.subheader("Tu resultado:")
st.markdown("Si no tienes la conexión real, escribe tu código usando `st.code()` para demostrar cómo lo harías teóricamente.")

# ESTUDIANTE: Escribe tu código (o tu st.code teórico) a continuación

MONGO_URI = st.secrets["mongo"]["uri"]


@st.cache_resource 
def init_connection():
    return MongoClient(MONGO_URI)

try:
    client = init_connection()
    
    db = client["Veterinaria"]
    collection = db["mascotas"]

    documentos = list(collection.find())

    if documentos:
        df_mongo = pd.DataFrame(documentos)

        if '_id' in df_mongo.columns:
            df_mongo = df_mongo.drop(columns=['_id'])

        st.success("¡Conexión exitosa y datos cargados!")
        
        st.write("Datos de la colección 'mascotas':")
        st.dataframe(df_mongo)
    else:
        st.warning("La conexión funciona, pero la colección parece estar vacía.")

except Exception as e:
    st.error(f"Error al conectar con MongoDB Atlas: {e}")
    



