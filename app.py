import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set judul halaman
st.title("Aplikasi Web Statistik")

# Tambahkan deskripsi atau penjelasan singkat
st.write("Ini adalah aplikasi web sederhana untuk menampilkan statistik dasar.")

# Muat data dari file CSV
data = pd.read_csv("data.csv")

# Tampilkan tabel data
st.subheader("Tabel Data")
st.dataframe(data)

# Tampilkan deskripsi statistik
st.subheader("Deskripsi Statistik")
st.write(data.describe())

# Tampilkan histogram
st.subheader("Histogram")
selected_column = st.selectbox("Pilih kolom:", data.columns)
plt.hist(data[selected_column].dropna())
st.pyplot(plt)

# Tampilkan scatter plot
st.subheader("Scatter Plot")
x_column = st.selectbox("Pilih kolom x:", data.columns)
y_column = st.selectbox("Pilih kolom y:", data.columns)
plt.scatter(data[x_column], data[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
st.pyplot(plt)


st.title('Thank uuu :v')