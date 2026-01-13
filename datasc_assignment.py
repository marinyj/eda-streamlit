import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io 

st.set_page_config(page_title="Analyze Your Data", page_icon="🔎", layout="wide")

st.title("📋 Analyze Your Data")
st.write("📁 Upload A **CSV** Or An **Excel** File To Explore Your Data Interactively!")

# ---------------- FILE UPLOAD ---------------- #
uploaded_file = st.file_uploader("Upload A CSV Or An Excel File", type=["csv","xlsx", "xls"])

if uploaded_file is not None:
    # -------- TASK 1: HANDLE CSV & EXCEL -------- #
    file_extension = uploaded_file.name.split(".")[-1]

    if file_extension == "csv":
        data = pd.read_csv(uploaded_file)
    elif file_extension in ["xlsx", "xls"]:
        data = pd.read_excel(uploaded_file)
    else:
        st.error("Could Not Read Excel/CSV File. Please Check The File Format")
        st.stop()
    
    # Convert boolean columns to string
    bool_cols = data.select_dtypes(include=["bool"]).columns
    data[bool_cols] = data[bool_cols].astype("str")

    st.success("File Uploaded Successfully! ✅")

    # ---------------- DATA PREVIEW ---------------- #
    st.write("### Preview Of Data")
    st.dataframe(data.head())

    # ---------------- DATA OVERVIEW ---------------- #
    st.write("###  Data Overview")
    st.write("Number of Rows :",data.shape[0])
    st.write("Number of Columns :",data.shape[1])
    st.write("Number of Missing Values :",data.isnull().sum().sum())
    st.write("Number of Duplicated Records :",data.duplicated().sum())

    # ---------------- DATA INFO ---------------- #
    st.write("### Complete Summary of Dataset")
    buffer = io.StringIO()
    data.info(buf=buffer)
    i = buffer.getvalue()
    st.text(i)

    # ---------------- NUMERICAL SUMMARY ---------------- #
    st.write("### 📃 Statistical Summary of Numerical Features in Dataset")
    st.dataframe(data.describe())

    # -------- TASK 2: CONDITIONAL NON-NUMERICAL SUMMARY -------- #
    non_numeric_cols = data.select_dtypes(include=["object", "bool"]).columns
    
    if len(non_numeric_cols) > 0:
        st.write("### 📑 Statistical Summary of Non-Numerical Features in Dataset")
        st.dataframe(data.describe(include=["bool","object"]))
    else:
        st.info("ℹ️ No Non-Numerical Features Found In This Dataset")
    
    # ---------------- COLUMN SELECTION ---------------- #
    st.write("### ✏️ Select The Desired Columns For Analysis")
    selected_columns = st.multiselect("Choose Columns",data.columns.tolist())

    if selected_columns:
        st.dataframe(data[selected_columns].head())
    else:
        st.info("No Columns Selected. Showing Full Dataset")
        st.dataframe(data.head())

    # ---------------- VISUALIZATION ---------------- #
    st.write("### 📊 Data Visualisation")
    st.write("Select **Columns** For Data Visualisation")

    columns = data.columns.tolist()
    x_axis = st.selectbox("Select Column For X-Axis", options=columns)
    y_axis = st.selectbox("Select Column For Y-Axis", options=columns)

    # Create Buttoms For Different Types Of Charts
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        line_btn = st.button("📈 Line Chart")
    with col2:
        scatter_btn = st.button("🔵 Scatter Plot")
    with col3:
        bar_btn = st.button("📊 Bar Chart")
    with col4:
        hist_btn = st.button("📶 Histogram")
    with col5:
        box_btn = st.button("📦Box Plot")


    # -------- LINE CHART -------- #
    if line_btn:
        fig,ax = plt.subplots()
        ax.plot(data[x_axis], data[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"Line Graph Of {x_axis} Vs {y_axis}")
        st.pyplot(fig) # show the graph


    # -------- SCATTER PLOT -------- #
    if scatter_btn:
        fig,ax = plt.subplots()
        ax.scatter(data[x_axis], data[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"Scatter Plot Of {x_axis} Vs {y_axis}")
        st.pyplot(fig) # show the graph

    # -------- BAR CHART -------- #
    if bar_btn:
       fig, ax = plt.subplots()
       ax.bar(data[x_axis].astype(str), data[y_axis])
       ax.set_title(f"Bar Chart: {x_axis} vs {y_axis}")
       ax.set_xlabel(x_axis)
       ax.set_ylabel(y_axis)
       plt.xticks(rotation=45)
       st.pyplot(fig)

    # -------- HISTOGRAM -------- #
    if hist_btn:
        if pd.api.types.is_numeric_dtype(data[x_axis]):
            fig, ax = plt.subplots()
            ax.hist(data[x_axis], bins=20)
            ax.set_title(f"Histogram of {x_axis}")
            ax.set_xlabel(x_axis)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
        else:
            st.warning("Histogram requires a numerical column.")

    # -------- BOX PLOT -------- #
    if box_btn:
        if pd.api.types.is_numeric_dtype(data[y_axis]):
            fig, ax = plt.subplots()
            ax.boxplot(data[y_axis])
            ax.set_title(f"Box Plot of {y_axis}")
            ax.set_ylabel(y_axis)
            st.pyplot(fig)
        else:
            st.warning("Box plot requires a numerical column.")

else:
    st.info("Please Upload A CSV Or An Excel File To Get Started")




