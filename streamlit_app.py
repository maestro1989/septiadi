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
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
  st.write('Menampilkan Dataframe dengan St AgGrid')




if __name__ == '__main__' : 
  main()
