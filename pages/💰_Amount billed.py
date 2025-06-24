import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

if "selected_name" in st.session_state:
    st.write(f"Selected employee: {st.session_state['selected_name']}")
else:
    st.write("No name selected yet.")

if 'sheet' in st.session_state and 'selected_name' in st.session_state:
    sheet = st.session_state['sheet']
    person_name = st.session_state['selected_name']

    person_data = sheet[sheet["Name"] == person_name]

    st.header(f"Amount billed by {person_name} per month")


    billed_amount = person_data.groupby('Activity_Date')['Amount'].sum()
    fig = px.line(billed_amount, title=f'Billed Amount for {person_name}')
    
    # Display the plot
    st.plotly_chart(fig)
    st.write(" ")
    st.write(f"Total amount billed by '{person_name}' in year is {billed_amount.sum()}")

    
