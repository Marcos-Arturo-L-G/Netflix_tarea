import pandas as pd
import numpy as np
import streamlit as st

st.title('Netflix data')

st.subheader('Integrantes: Marcos Arturo Lopez Gonzalez')
st.subheader('Jose Obed Mariano Hipolito ')

DATA_URL = ('https://raw.githubusercontent.com/Marcos-Arturo-L-G/Netflix_tarea/master/movies.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    return data

Todas_pelis = st.sidebar.checkbox("Mostrar todas las peliculas ")
if Todas_pelis:
  data = load_data(2000)
  st.text("Cargado! (usando st.cache)")
  st.dataframe(data)


@st.cache
def load_data_byname(nombre):
  datafiltered = load_data(2000)
  filtered_byname = datafiltered[datafiltered['name'].str.contains(nombre)]
  return filtered_byname

titulo = st.sidebar.text_input('Titulo de la pelicula: ')
btnFilteredbyname = st.sidebar.button('Buscar')

if (btnFilteredbyname):
  filterbyname = load_data_byname(titulo)
  count_row = filterbyname.shape[0]
  st.write(f'Total de peliculas: {count_row}')
  st.dataframe(filterbyname)


@st.cache
def load_data_bydirec(director):
  data = load_data(2000)
  filtered_data_bydirec = data[data['director'] == director]
  return filtered_data_bydirec

data = load_data(2000)
selected = st.sidebar.selectbox("Selecciona el director", data['director'].unique())
btnFilterBydirec = st.sidebar.button('Filtrar')

if (btnFilterBydirec): 
  st.write("Peliculas dirigidas por "+selected)
  filterbydirec = load_data_bydirec(selected)
  count_row = filterbydirec.shape[0]
  st.write(f'Total Peliculas: {count_row}')
  st.dataframe(filterbydirec)
