# Mebgimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Membuat judul
st.title('Prediksi Breast Cancer')

# Menambah subheader
st.subheader('Selamat datang di Data Science Deployment')

# Load model
my_model = pickle.load(open('model_prediksi_breast_cancer3.pkl', 'rb'))


# Menulis text (ukuran kecil)
st.write('Silahkan masukkan data Pasien')

# Baris Pertama
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        radius_mean = st.number_input('radius_mean', value=1012)
    with col2:
        texture_mean = st.number_input('texture_mean', value=1012)
    with col3:
        perimeter_mean = st.number_input('perimeter_mean', value=1012)
        

# Baris Kedua
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        area_mean = st.number_input('area_mean', value=1012)
    with col2:
        smoothness_mean = st.number_input('smoothness_mean', value=1012)
    with col3:
        compactness_mean = st.number_input('compactness_mean', value=1012)
        

# Baris Ketiga
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        concavity_mean = st.number_input('concavity_mean', value=1012)
    with col2:
        concave_points_mean = st.number_input('concave_points_mean', value=1012)
    with col3:
        symmetry_mean = st.number_input('symmetry_mean', value=1012)


# Baris Keempat
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        fractal_dimension_mean = st.number_input('fractal_dimension_mean', value=1012)
    with col2:
        radius_se = st.number_input('radius_se', value=1012)
    with col3:
        texture_se = st.number_input('texture_se', value=1012)

# Baris Kelima
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        perimeter_se = st.number_input('perimeter_se', value=1012)
    with col2:
        area_se = st.number_input('area_se', value=1012)
    with col3:
        smoothness_se = st.number_input('smoothness_se', value=1012)

# Baris Keenam
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        compactness_se = st.number_input('compactness_se', value=1012)
    with col2:
        concavity_se = st.number_input('concavity_se', value=1012)
    with col3:
        concave_points_se = st.number_input('concave_points_se', value=1012)

# Baris Ketujuh
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        symmetry_se = st.number_input('symmetry_se', value=1012)
    with col2:
        fractal_dimension_se = st.number_input('fractal_dimension_se', value=1012)
    with col3:
        radius_worst = st.number_input('radius_worst', value=1012)
        

# Baris Kedelapan
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        texture_worst = st.number_input('texture_worst', value=1012)
    with col2:
        perimeter_worst = st.number_input('perimeter_worst', value=1012)
    with col3:
        area_worst = st.number_input('area_worst', value=1012)
        
# Baris Kesembilan
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        smoothness_worst = st.number_input('smoothness_worst', value=1012)
    with col2:
        compactness_worst = st.number_input('compactness_worst', value=1012)
    with col3:
        concavity_worst = st.number_input('concavity_worst', value=1012)
        

# Baris Kesepuluh
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        concave_points_worst = st.number_input('concave_points_worst', value=1012)
    with col2:
        symmetry_worst = st.number_input('symmetry_worst', value=1012)
    with col3:
        fractal_dimension_worst = st.number_input('fractal_dimension_worst', value=1012)
        
#code untuk prediksi
cancer_diagnosis =''

#membuat tombol prediksi
if st.button('Tes rprediksi Keganasan Breast Cancer'):
    cancer_predict = my_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])


    if (cancer_predict[0] == 1):
        cancer_diagnosis = 'Cancer Ganas'
    else :
        cancer_diagnosis = 'Cancer  Jinak'
        
    st.success(cancer_diagnosis)