# Imports
import streamlit as st #type:ignore
import pandas as pd  #type:ignore
import os
from io import BytesIO

# Set up Our App
st.set_page_config(page_title="💽 Data Sweeper", layout="wide")
st.title("💽 Data Sweeper")
st.write("Upload and visualize your data without limitations!")

# Upload File
uploaded_files = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read File
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue  # Skip unsupported files

        # Display File Info
        st.write(f"**📁 File Name:** {file.name}")
        st.write(f"**📏 File Size:** {file.size/1024:.2f} KB")

        # Show Data Preview
        st.subheader("🔍 Data Preview")
        st.dataframe(df.head())

        # **Column Selection**
        st.subheader("📌 Select Columns to Keep")
        selected_columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]

        # **Data Visualization**
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.line_chart(df.select_dtypes(include="number"))  # No limits, show all numeric columns

        # **Convert the file (CSV to Excel)**
        st.subheader("🔁 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"Convert {file.name} to {conversion_type}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                filename = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"

            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False, engine="openpyxl")
                filename = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"⬇️ Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=filename,
                mime=mime_type,
            )
