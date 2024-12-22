import streamlit as st
import pandas as pd
from pyspark.sql import SparkSession

# Membuat Spark session
spark = SparkSession.builder \
    .appName("Streamlit with Spark") \
    .getOrCreate()

# Path ke file CSV
file_path = "NameDanPrice.csv"  # Ganti dengan path yang sesuai

# Membaca dataset dari file CSV ke DataFrame Spark
spark_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Judul aplikasi
st.title("Daftar Harga Game")

# Mengonversi DataFrame Spark ke Pandas untuk ditampilkan di Streamlit
pandas_df = spark_df.toPandas()

# Menampilkan tabel
st.write("Tabel Harga Game:")
st.dataframe(pandas_df)

# Menampilkan histogram harga
st.write("Distribusi Harga Game:")
st.bar_chart(pandas_df['price'])