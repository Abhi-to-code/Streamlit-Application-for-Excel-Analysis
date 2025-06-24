import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Exercise Excel",
    page_icon="📝"
)

st.title("Exercise Excel Sheet Analyser...")
st.sidebar.success("Select an analysis above.")

uploaded_file = st.file_uploader("Upload Excel File", type=['xlsx'])

if uploaded_file is not None:
# Read the Excel file and store it in session_state if not already done
    if 'sheet' not in st.session_state:
        sheet = pd.read_excel(uploaded_file)
        sheet = sheet.drop(sheet.columns[0], axis=1)
        st.session_state['sheet'] = sheet
    else:
        sheet = st.session_state['sheet']

    st.header("The excel taken for the analysis is:")
    st.write(sheet)

    sheet_name = sheet["Name"]
    all_names = sheet_name.unique()
    all_names = np.array(all_names)

    st.header("Select an employee for their analysis: ")

    st.session_state["selected_name"] = st.selectbox(label="Select your name: ", options=all_names)
    st.write(st.session_state["selected_name"])

# You can now access st.session_state["sheet"] in any other part of the app
# For example, on another page, you can retrieve the DataFrame like this:
# sheet = st.session_state['sheet']

# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")

# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)
