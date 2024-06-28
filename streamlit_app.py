import streamlit as st 
import pandas as pd 
#import requests
#from st_aggrid import AgGrid

#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 
  st.write('Minimal Example')

if __name__ == '__main__' : 
  main()

def main() : 
  st.header('Halaman Streamlit Septiadi')
  st.subheader('Ini Sub Judul')
  st.markdown('### Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' : 
  main()

def main() : 
  st.write('Contoh dataframe')
  st.dataframe(house)
  st.metric(label="Temperature", value="70 °F", delta="-1.2 °F")
  # Menampilkan metrik kedua
  st.metric(label="Wind Speed", value="15 mph", delta="-2 mph")
  # Menampilkan metrik ketiga tanpa delta
  st.metric(label="Humidity", value="85%")
  # Menampilkan metrik dengan warna delta disesuaikan
  st.metric(label="Stock Price", value="$300", delta="-5%", delta_color="normal")




if __name__ == '__main__' : 
  main()
