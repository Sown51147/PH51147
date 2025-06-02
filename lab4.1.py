# Section 1
import streamlit as st

st.title("Đếm tần suất từ xuất hiện trong văn bản")

file = st.file_uploader("Chọn file văn bản")
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

    van_ban = ""
    for tu, so_luong in tan_suat.items():
        van_ban += f'{tu}: {so_luong}\n' 
    
    st.download_button(
        label="Tải file về",
        data = van_ban,
        file_name="file_tai_ve.txt",
        mime="text/plain"
    )

# Section 2

st.header("Hiển thị file tần suất")

file_tan_suat = st.file_uploader("Chọn file tần suất")

if file_tan_suat is not None:
    noi_dung = file_tan_suat.read().decode("utf-8")
    tan_suat_tu = {}
    for dong in noi_dung.strip().split("\n"):
        if ":" in dong:
            tu,so_luong = dong.split(":")
            tan_suat_tu[tu.strip()] = int(so_luong.strip())
    st.subheader("Tần suất từ")
    st.write(tan_suat_tu)