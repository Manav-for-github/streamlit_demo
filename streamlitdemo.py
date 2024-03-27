import streamlit as st


Name =st.text_input('Enter Your Name:')
Fname = st.text_input('Enter Your Father name:')
Adr =st.text_area('Enter Your Text:')
Classdata = st.selectbox('Enter Your Class:',(1,2,3,4,5,6,7,8,9,10,11,12))

Button =st.button('Done')
if Button :
    st.markdown(f'''
    Name: {Name}
    Father Name: {Fname}
    Address: {Adr}
    Class: {Classdata}''')