import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
clean_df = pd.read_csv('clean_df.csv')

# Judul (Header)
st.set_page_config(page_title="Dashboard Bike Sharing", page_icon="🚴", layout="wide")
st.title("Dashboard Bike Sharing 🚴")

# Sidebar
st.sidebar.title("Data Visualization")

# Filter berdasakan Tahun
year = st.sidebar.selectbox("Filter Berdasarkan Tahun", options=[2011, 2012])

# Update dataset berdasarkan tahun yang dipilih
filtered_df = clean_df[clean_df['yr'] == (year - 2011)]  # Filter 0 for 2011, 1 for 2012

# KPI: Jumlah Total Penyewa Casual, Registered, dan Total Sepeda yang disewa (cnt)

# Menghitung total casual, registered, dan total sewa (cnt)
total_casual = filtered_df['casual'].sum()
total_registered = filtered_df['registered'].sum()
total_rentals = filtered_df['cnt'].sum()

# Menampilkan KPI dalam tiga kolom
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Pengguna Casual", value=f"{total_casual:,.0f}")

with col2:
    st.metric(label="Total Pengguna Registered", value=f"{total_registered:,.0f}")

with col3:
    st.metric(label="Total Sepeda yang Disewa", value=f"{total_rentals:,.0f}")

# 1. Tren Sewa Sepeda per Bulan di tahun terpilih
st.subheader(f"Monthly Bike Rentals in {year}")
monthly_rentals = filtered_df.groupby('mnth')['cnt'].sum()
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly_rentals.index, monthly_rentals.values, marker='o')
ax.set_title(f'Tren Sewa Sepeda per Bulan di Tahun {year}', fontsize=16)
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Sewa')
ax.grid()
st.pyplot(fig)

# 2. Perbandingan Jumlah Pengguna di Hari Libur dan di Hari Biasa
# 3. Perbandingan Pengguna Casual dan Registered di Hari Kerja
st.subheader("Customer Demographic")
col1, col2 = st.columns(2)

with col1:
    total_rentals_workingday = filtered_df[filtered_df['workingday'] == 1]['cnt'].sum()
    total_rentals_holiday = filtered_df[filtered_df['holiday'] == 1]['cnt'].sum()
    labels = ['Hari Kerja', 'Hari Libur']
    sizes = [total_rentals_workingday, total_rentals_holiday]
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('Pengguna Sepeda di Hari Kerja dan Hari Libur', fontsize=18)
    ax.axis('equal')
    st.pyplot(fig)

with col2:
    workingday_rentals = filtered_df[filtered_df['workingday'] == 1]
    total_casual = workingday_rentals['casual'].sum()
    total_registered = workingday_rentals['registered'].sum()
    labels = ['Casual', 'Registered']
    totals = [total_casual, total_registered]
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(totals, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('Pengguna Casual dan Registered pada Hari Kerja', fontsize=18)
    ax.axis('equal')
    st.pyplot(fig)

# 4. Pengguna Sepeda per Musim
# 5. Jumlah Sewa Sepeda  Berdasarkan Kondisi Cuaca
col1, col2 = st.columns(2)

with col1:
    season_rentals = filtered_df.groupby('season')['cnt'].sum()
    season_labels = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']
    colors = ['C0'] * len(season_rentals)
    max_index = season_rentals.idxmax()
    colors[max_index - 1] = 'C1'
    fig, ax = plt.subplots(figsize=(8, 5))
    season_rentals.plot(kind='bar', color=colors, ax=ax)
    ax.set_title('Jumlah Sewa Sepeda per Musim', fontsize=20)
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Sewa')
    ax.set_xticks(range(len(season_labels)))
    ax.set_xticklabels(season_labels, rotation=0)
    st.pyplot(fig)

with col2:
    weather_rentals = filtered_df.groupby('weathersit')[['casual', 'registered']].sum()
    weather_labels = ['Cerah', 'Berkabut', 'Hujan Ringan']
    fig, ax = plt.subplots(figsize=(10, 6))
    weather_rentals.plot(kind='bar', color=['C0', 'C1'], ax=ax)
    ax.set_title('Jumlah Sewa Berdasarkan Kondisi Cuaca', fontsize=20)
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Sewa')
    ax.set_xticks(range(len(weather_labels)))
    ax.set_xticklabels(weather_labels, rotation=0)
    ax.legend(title='Tipe Pengguna')
    st.pyplot(fig)

# 6. Pengaruh Kecepatan Angin Terhadap Sewa Sepeda
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(filtered_df['windspeed'], bins=20, alpha=0.7, color='C0')
ax.set_title(f'Pengaruh Kecepatan Angin terhadap Sewa Sepeda di Tahun {year}', fontsize=14)
ax.set_xlabel('Kecepatan Angin')
ax.set_ylabel('Jumlah Sewa')
ax.grid(axis='y')
st.pyplot(fig)