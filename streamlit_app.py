import streamlit as st 

def main() : 
  st.write('Minimal Example')

if __name__ == '__main__' : 
  main()

def maingame() : 
  st.header('Ini Judul')
  st.subheader('Ini Sub Judul')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' : 
  maingame()
