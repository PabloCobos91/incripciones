import streamlit as st
import csv
from PIL import Image

##########################################################################
image = Image.open('C:/Users/LENOVO/Desktop/PROYECTO_SCRUM/TEORIA.png')
image = image.resize((1350,450))
st.image(image)

def enter_data (first_name, last_name_1, last_name_2, correo_electronico, telefono, titulacion):
    
    if st.button("Leer términos y condiciones"):
        st.write("Duración completa del curso: 30H")
        st.write ("Al aceptar queda comprometido a los horarios establecidos.")
        st.write ("Sus datos de registros son privados y de uso exclusivo para acceso a campos virtual.")
    accepted = st.checkbox("Acepto los términos y condiciones")
    if accepted:
        if first_name and last_name_1 and last_name_2 and titulacion and correo_electronico and telefono :
            if st.button ("Ingresar datos"):
                data = [first_name, last_name_1, last_name_2, correo_electronico, telefono, titulacion, ]
                save_data(data)
                st.write("Datos guardados correctamente.")
                st.write("---------------------------------------------")
        else:
            st.warning("Todos los campos son requeridos.")
    else:
        st.warning("No ha aceptado términos y condiciones. Acéptelos para poder ingresar sus datos. ")
##########################################################################

##########################################################################
#ABRIR_ARCHIVOS
def save_data(data):
    with open('alumnos_maquinas.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


##########################################################################


##########################################################################
#WIDGETS
st.subheader("Informacion del alumno")
first_name = st.text_input ("Nombre")
last_name_1 = st.text_input ("Primer apellido")
last_name_2 = st.text_input ("Segundo apellido")
correo_electronico = st.text_input("Correo electrónico")
telefono =  st.text_input("Número de teléfono")
titulacion = st.selectbox("Titulación:" ,
    ["Ingeniería en Diseño Industrial y Desarrollo del Producto", 
     "Ingeniería Eléctrica", 
     "Ingeniería en Electrónica Industrial", 
     "Ingeniería Mecánica", 
     "Ingeniería en Tecnologías Industriales"])
##########################################################################

##########################################################################
#Incripción
st.subheader("Inscripción del curso")

enter_data(first_name, last_name_1, last_name_2, correo_electronico, telefono, titulacion)
