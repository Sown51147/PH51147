import streamlit as st

st.title("Đếm tần suất từ xuất hiện trong văn bản")

file = st.file_uploader("Chọn file VĂN BẢN")
if file is not None:
    noi_dung = file.read().decode("utf-8") 
    noi_dung = noi_dung.lower()
    noi_dung = noi_dung.replace(",","").replace(".","")
    danh_sach_tu = noi_dung.split()

    tan_suat = {}
    for tu in danh_sach_tu:
        if tu in tan_suat:
            tan_suat[tu] += 1
        else:
            tan_suat[tu] = 1

    st.write("Tần suất các từ:", tan_suat)