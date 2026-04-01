import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Time Series Noise Reduction Dashboard")

# Sidebar
st.sidebar.header("Options")

menu = st.sidebar.radio(
    "Select Option",
    ["Upload Data", "Show Original Data"]
)

# File upload
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

# Store data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state["data"] = df

# -------------------------------
# OPTION 1: Upload Data
# -------------------------------
if menu == "Upload Data":
    st.write("### 📁 Upload Your Noisy Data")

    if "data" in st.session_state:
        df = st.session_state["data"]

        st.success("File uploaded successfully ✅")
        st.write(df.head())

    else:
        st.warning("Please upload a CSV file from sidebar")

# -------------------------------
# OPTION 2: Show Original + Graph
# -------------------------------
elif menu == "Show Original Data":

    if "data" in st.session_state:
        df = st.session_state["data"]

        st.write("### 📄 Original Data")
        st.write(df)

        # Column selection
        column = st.selectbox("Select Column", df.columns)

        data = df[column]

        # Moving average
        window = st.slider("Select Moving Average Window", 2, 10, 3)
        smooth = data.rolling(window=window).mean()

        # Graph
        st.write("### 📈 Graphical Representation")

        fig, ax = plt.subplots()

        ax.plot(data, label="Original Data", marker='o')
        ax.plot(smooth, label="Smoothed Data", marker='o')

        ax.set_title("Noise Reduction using Moving Average")
        ax.set_xlabel("Index")
        ax.set_ylabel("Values")
        ax.legend()

        st.pyplot(fig)

    else:
        st.warning("Please upload data first ⚠️")