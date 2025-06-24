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

    billable_hours = person_data[person_data['Billable'] == 'Yes']['Duration'].sum()
    non_billable_hours = person_data[person_data['Billable'] == 'No']['Duration'].sum() 

    st.header(f"Analysis in hours spent on Billabes and non-billables by {person_name}")

    fig1 = px.pie(
        names=['Billable Hours', 'Non-Billable Hours'],
        values=[billable_hours, non_billable_hours],
        title=f'Billable vs Non-Billable Hours for {person_name}',
        color_discrete_sequence=['sky blue', 'yellow']
    )
    st.write(fig1)
    st.write("")
    st.write(f"Total hours spent on billables by '{person_name}' is {billable_hours}")
    st.write(f"Total hours spent on non-billables by '{person_name}' is {non_billable_hours}")

    st.header(f"Analysis on no.of Billabes and non-billables by {person_name}")

    billables = person_data[person_data["Billable"] == "Yes"]
    total_billables = len(billables)

    non_billables = person_data[person_data["Billable"] == "No"]
    total_non_billables = len(non_billables)


    fig2 = px.pie(
        names=['Total Billables', 'Total Non-Billable'],
        values=[total_billables, total_non_billables],
        title=f'Total no.of Billable vs Non-Billable done by {person_name}',
        color_discrete_sequence=['sky blue', 'yellow']
    )
    st.write(fig2)
    st.write(" ")
    st.write(f"Total no.of Billables done by '{person_name} is {total_billables}'")
    st.write(f"Total no.of non billables done by '{person_name} is {total_non_billables}'")
