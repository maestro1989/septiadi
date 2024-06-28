import streamlit as st 
import pandas as pd 
#import requests
#from st_aggrid import AgGrid
import plotly.express as px 
import matplotlib.pyplot as plt

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
  st.write('Contoh dataframe dengan AgGrid')
  #AgGrid (house)
  st.table([x for x in range(1,5)])

def main() : 
    #matplotlib chart 
    fig,ax = plt.subplots()
    plt.scatter(house['price'],house['bedrooms'])
    st.pyplot(fig)
    plotly_fig = px.scatter(house['price'],house['bedrooms'])
    st.plotly_chart(plotly_fig)
if __name__ == '__main__' : 
    main()

if __name__ == '__main__' : 
  main()
