import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

if "selected_name" in st.session_state:
    st.write(f"Selected employee: {st.session_state["selected_name"]}")
else:
    st.write("No name selected yet.")

if 'sheet' in st.session_state and 'selected_name' in st.session_state:
    sheet = st.session_state['sheet']
    person_name = st.session_state['selected_name']

    person_data = sheet[sheet["Name"] == person_name]

    st.header(f"Duration spent on work items by {person_name}: ")

    work_item_person = person_data.groupby('Work Items')['Duration'].sum()
    #work_item_person_duration = person_data.groupby('Work Items')['Activity_Date'].sum()

    fig = px.bar(work_item_person)
    st.plotly_chart(fig)
    st.write("")

    st.header(f"Duration spent on Product Services by {person_name}")

    total_time_per_product_service = person_data.groupby('Product_Service')['Duration'].sum()

    fig = px.bar(total_time_per_product_service)
    st.plotly_chart(fig)
    st.write("")

    st.header(f"Duration spent on Catagories by {person_name}")

    total_time_per_category = person_data.groupby('Category')['Duration'].sum()

    fig = px.bar(total_time_per_category)
    st.plotly_chart(fig)
    
