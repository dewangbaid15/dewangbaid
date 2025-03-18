import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Dewangs\'s First Dashboard in Python')

st.sidebar.title('Want to know more:')
section = st.sidebar.radio('Go to:', ['Home', 'Data Table', 'Bar Chart'])

data= pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23,17,35,29]
    })


if section == 'Home':
    st.write('Welcome to the f dashboard! Please select a section from the sidebar.')
    st.write('The next line.....')
    
elif section == 'Data Table':
    st.subheader('Data Table')
    st.write(data)
    
elif section == 'Bar Chart':
    st.subheader ('Bar Chart')
    fig, ax= plt.subplots()
    ax.bar(data['Category'], data['Values'])
    ax.set_xlabel('Category')
    ax.set_ylabel('Values')
    st.pyplot(fig)
    

