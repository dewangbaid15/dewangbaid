import streamlit as stimport pandas as pdimport matplotlib.pyplot as pltst.title('Dewangs\'s First Dashboard in Python')data= pd.DataFrame({    'Category': ['A', 'B', 'C', 'D'],    'Values': [23,17,35,29]})tab1, tab2, tab3 = st.tabs(['Home', 'Data Table', 'Bar Chart'])with tab1:    st.write('Welcome to the f dashboard! Please select a section from the sidebar.')    with tab2:    st.subheader('Data Table')    st.write(data)    with tab3:    st.subheader ('Bar Chart')    st.bar_chart(data.set_index('Category'))    