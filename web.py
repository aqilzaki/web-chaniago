import streamlit as st
import pandas as pd

nama_file = 'datachaniago.xlsx'

df = pd.ExcelWriter(nama_file)

kg = st.text_input('masukan angka: ')
event  = st.button('submit')
event1 = st.button('cancel')
while True:
    if event == True:
        df = df._write_cells(row=1, ingnore_index = True)
        df.to_excel(nama_file, index=False)
        st.success('berhasil')
    if event1 == True:
        break