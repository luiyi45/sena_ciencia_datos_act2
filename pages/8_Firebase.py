import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

st.title("Bases de Datos en la Nube: Firebase Firestore")

st.markdown("""
### Ejercicio
Firebase es otra opción excelente adoptada por múltiples startups para almacenar datos en tiempo real.

**Instrucciones:**
1. Asume que se te proporcionó un archivo de credenciales de servicio `llave_secreta.json`.
2. Escribe el **código teórico (usando st.code() o conectándote si tienes tu propia bd)** que emplearías con `firebase_admin` para arrancar la aplicación y obtener el cliente de la base de datos.
3. El objetivo sería conectarse a la colección `vehiculos` de tu Firestore y traer todos los documentos.
4. Indica cómo convertirías la respuesta iterando los documentos para extraer su `to_dict()`.
5. Convierte esa lista a un DataFrame `df_firebase` final.
""")

st.subheader("Tu resultado:")
st.markdown("Escribe en la parte de abajo el código que usarías para lograr el objetivo. Si usas código comentado/teórico, compártelo adentro de `st.code()`.")

# ESTUDIANTE: Escribe tu código a continuación


if not firebase_admin._apps:
    try:
        cred = credentials.Certificate("llave_secreta.json")
        firebase_admin.initialize_app(cred)
    except Exception as e:
        st.error(f"Error al cargar la llave: {e}")

db = firestore.client()

st.subheader("Tu resultado:")

try:
    vehiculos_ref = db.collection("vehiculos")
    docs = vehiculos_ref.get()

    lista_vehiculos = [doc.to_dict() for doc in docs]

    if lista_vehiculos:
        df_firebase = pd.DataFrame(lista_vehiculos)
        
        st.success("Datos traídos exitosamente de Firestore")
        st.dataframe(df_firebase)
    else:
        st.warning("No se encontraron documentos en la colección 'vehiculos'.")

except Exception as e:
    st.info("Simulación: Si no esta el archivo JSON")
    


