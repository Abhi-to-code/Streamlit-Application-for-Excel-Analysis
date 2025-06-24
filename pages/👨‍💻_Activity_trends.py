import streamlit as st
import pandas as pd
import plotly.express as px

if "selected_name" in st.session_state:
    st.write(f"Selected name: {st.session_state["selected_name"]}")
else:
    st.write("No name selected yet.")


if 'sheet' in st.session_state and 'selected_name' in st.session_state:
    sheet = st.session_state['sheet']
    person_name = st.session_state['selected_name']
    
    person_data = sheet[sheet["Name"] == person_name]

    # Group by Activity_Date and sum the Duration
    total_activity_trends = person_data.groupby('Activity_Date')['Duration'].sum()
    avg_activity_trends = person_data.groupby('Activity_Date')['Duration'].mean()

    st.header(f"Total time spent by {person_name} in year 2023")
    fig = px.line(total_activity_trends, title=f'Activity Trends for {person_name}', labels={'x': 'Activity Date', 'y': 'Duration'},)
    #fig.update_layout(width=1000, height=600)
    st.plotly_chart(fig)
    sheet['Duration'] = pd.to_numeric(sheet['Duration'], errors='coerce')
    total_time_per_individual = sheet.groupby('Name')['Duration'].sum()

    person_duration = total_time_per_individual.loc[person_name]
    st.write(f"The Total duration of '{person_name}' worked in a year is {person_duration} hours")
    st.write("")

    st.header(f"Average time spent by {person_name} in year 2023")
    fig = px.line(avg_activity_trends, title=f'Activity Trends for {person_name}', labels={'x': 'Activity Date', 'y': 'Duration'},)
    #fig.update_layout(width=1000, height=600)
    st.plotly_chart(fig)
    st.write("")
    avg_duration_per_ind = sheet.groupby('Name')['Duration'].mean()
    avg_duration = avg_duration_per_ind.loc[person_name]

    st.write(f"The avg duration of '{person_name}' worked in a year is {avg_duration} hours")  

else:
    st.write("Please select an employee on the main page.")