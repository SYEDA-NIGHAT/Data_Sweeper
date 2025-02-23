# imports

# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO


# # Set up Our App

# st.set_page_config(page_title="💽 Data sweeper", layout="wide")
# st.title("💽 Data sweeper")
# st.write("Welcome to datasweeper!")
# st.write(
#     "Transform your file between CSV and Excel format with built-in data cleaning and visualisation."
# )

# uploaded_files = st.file_uploader(
#     "Upload your CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=True
# )

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error("Unsupported file type {file_ext}")
#         continue

#     # Display info about the file

#     st.write(f"**File Name**{file.name}")
#     st.write(f"**File Size**{file.size/1024}")

#     # Show 5 rows of the data

#     st.write("Preview the Head of the Dataframe")
#     st.dataframe(df.head())

#     # Options for Data Cleaning

#     st.subheader("Data Cleaning Options")
#     if st.checkbox(f"Clean Data for {file.name}"):
#         col1, col2 = st.columns(2)

#         with col1:
#             if st.button(f"Remove Duplicates from {file.name}"):
#                 df = df.drop_duplicates(inplace=True)
#                 st.write("Duplicates Removed!")

#                 with col2:
#                     if st.button(f"Fill Missing Values for {file.name}"):
#                         numeric_cols = df.select_dtypes(include=["number"]).columns
#                         df[numeric_cols] = df[numeric_cols].fillna(
#                             df[numeric_cols].mean()
#                         )
#                         st.write("Missing Values Filled!")

#                         # Choose Specific columns to keep or convert

#                         st.subheader("Choose Columns to Keep or Convert")
#                         columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
#                         df = df[columns]
                        
#                     # Create some visualisations

#                     st.subheader("📊Data Visualisation")
#                     if st.checkbox(f"Show Visualisation for {file.name}"):
                        
                        
#                         # st.write("Visualising the Data")
#                         # st.write("Visualisation coming soon!")




# # imports
# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# # Set up Our App
# st.set_page_config(page_title="💽 Data Sweeper", layout="wide")
# st.title("💽 Data Sweeper")
# st.write("Welcome to Data Sweeper!")
# st.write(
#     "Transform your file between CSV and Excel format with built-in data cleaning and visualization."
# )

# uploaded_files = st.file_uploader(
#     "Upload your CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=True
# )

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#             continue  # Ensures the loop doesn't proceed if the file is unsupported

#     # Display info about the file
#     st.write(f"**File Name:** {file.name}")
#     st.write(f"**File Size:** {file.size/1024:.2f} KB")

#     # Show 5 rows of the data
#     st.write("Preview the Head of the DataFrame")
#     st.dataframe(df.head())

#     # Options for Data Cleaning
#     st.subheader("Data Cleaning Options")
#     if st.checkbox(f"Clean Data for {file.name}"):
#         col1, col2 = st.columns(2)

#         with col1:
#             if st.button(f"Remove Duplicates from {file.name}"):
#                 df = df.drop_duplicates()
#                 st.success("Duplicates Removed!")

#         with col2:
#             if st.button(f"Fill Missing Values for {file.name}"):
#                 numeric_cols = df.select_dtypes(include=["number"]).columns
#                 df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                 st.success("Missing Values Filled!")

#         # Choose Specific Columns to Keep or Convert
#         st.subheader("Choose Columns to Keep or Convert")
#         columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
#         df = df[columns]

#         # Create some visualizations
#         st.subheader("📊 Data Visualization")
#         if st.checkbox(f"Show Visualization for {file.name}"):
#             st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])
            
#         # Convert the file ->CSV to Excel
#         st.subheader("🔁Conversion Options")
#         conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
#         if st.button(f"Convert {file.name} to {conversion_type}"):
#             buffer = BytesIO()
#             if conversion_type == "CSV":
#              df.to_csv(buffer, index=False)
#              filename = file.name.replace("file_ext", ".csv")
#              mime_type = "text/csv"
         
#             elif conversion_type == "Excel":
#              buffer = BytesIO()
#              df.to_excel(buffer, index=False)
#              filename = file.name.replace("file_ext", ".xlsx")
#              mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         buffer.seek(0)
        
#         # Download Button
# st.download_button(
#     label=f"⬇️ Download {file.name} as {conversion_type}",
#     data=buffer,
#     file_name=filename,
#     mime=mime_type,
# )
# st.success("🎉 All files processed")



# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# # Set up Our App
# st.set_page_config(page_title="💽 Data Sweeper", layout="wide")
# st.title("💽 Data Sweeper")
# st.write("Welcome to Data Sweeper!")
# st.write("Transform your file between CSV and Excel format with built-in data cleaning and visualization.")

# uploaded_files = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#             continue  # Ensures the loop doesn't proceed if the file is unsupported

#         # Display info about the file
#         st.write(f"**File Name:** {file.name}")
#         st.write(f"**File Size:** {file.size/1024:.2f} KB")

#         # Show 5 rows of the data
#         st.write("Preview the Head of the DataFrame")
#         st.dataframe(df.head())

#         # Options for Data Cleaning
#         st.subheader("Data Cleaning Options")
#         if st.checkbox(f"Clean Data for {file.name}"):
#             col1, col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove Duplicates from {file.name}"):
#                     df = df.drop_duplicates()
#                     st.success("Duplicates Removed!")

#             with col2:
#                 if st.button(f"Fill Missing Values for {file.name}"):
#                     numeric_cols = df.select_dtypes(include=["number"]).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.success("Missing Values Filled!")

#             # Choose Specific Columns to Keep or Convert
#             st.subheader("Choose Columns to Keep or Convert")
#             columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
#             df = df[columns]

#             # Create some visualizations
#             st.subheader("📊 Data Visualization")
#             if st.checkbox(f"Show Visualization for {file.name}"):
#                 st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

#         # Convert the file -> CSV to Excel
#         st.subheader("🔁 Conversion Options")
#         conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

#         if st.button(f"Convert {file.name} to {conversion_type}"):
#             buffer = BytesIO()
#             if conversion_type == "CSV":
#                 df.to_csv(buffer, index=False)
#                 filename = os.path.splitext(file.name)[0] + ".csv"
#                 mime_type = "text/csv"

#             elif conversion_type == "Excel":
#                 df.to_excel(buffer, index=False, engine="openpyxl")
#                 filename = os.path.splitext(file.name)[0] + ".xlsx"
#                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

#             buffer.seek(0)

#             # Download Button (moved inside the loop)
#             st.download_button(
#                 label=f"⬇️ Download {file.name} as {conversion_type}",
#                 data=buffer,
#                 file_name=filename,
#                 mime=mime_type,
#             )




# # Imports
# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# # Set up the app
# st.set_page_config(page_title="💽 Data Sweeper", layout="wide")
# st.title("💽 Data Sweeper")
# st.write("Welcome to Data Sweeper! Transform your file between CSV and Excel format with built-in data cleaning and visualization.")

# # File upload
# uploaded_files = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#             continue  # Skip unsupported files

#     # Display file info
#     st.write(f"**File Name:** {file.name}")
#     st.write(f"**File Size:** {file.size/1024:.2f} KB")

#     # Show preview of data
#     st.write("Preview of the DataFrame")
#     st.dataframe(df.head())

#     # Data Cleaning Options
#     st.subheader("🧹 Data Cleaning Options")
#     if st.checkbox(f"Clean Data for {file.name}"):
#         col1, col2 = st.columns(2)

#         with col1:
#             if st.button(f"Remove Duplicates from {file.name}"):
#                 df = df.drop_duplicates()
#                 st.success("✅ Duplicates Removed!")

#         with col2:
#             if st.button(f"Fill Missing Values for {file.name}"):
#                 numeric_cols = df.select_dtypes(include=["number"]).columns
#                 df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                 st.success("✅ Missing Values Filled!")

#     # Column Selection
#     st.subheader("📌 Select Columns to Keep")
#     columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
#     df = df[columns]

#     # Data Visualization
#     st.subheader("📊 Data Visualization")
#     if st.checkbox(f"Show Visualization for {file.name}"):
#         numeric_cols = df.select_dtypes(include="number").columns
#         if len(numeric_cols) >= 2:
#             st.bar_chart(df[numeric_cols].iloc[:, :2])  # Show the first two numeric columns
#         else:
#             st.warning("⚠️ Not enough numerical columns for visualization.")

#     # File Conversion
#     st.subheader("🔁 File Conversion")
#     conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

#     if st.button(f"Convert {file.name} to {conversion_type}"):
#         buffer = BytesIO()
        
#         if conversion_type == "CSV":
#             df.to_csv(buffer, index=False)
#             filename = file.name.replace(file_ext, ".csv")
#             mime_type = "text/csv"
#         elif conversion_type == "Excel":
#             df.to_excel(buffer, index=False, engine="openpyxl")
#             filename = file.name.replace(file_ext, ".xlsx")
#             mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        
#         buffer.seek(0)
#         st.download_button(label=f"⬇️ Download {filename}", data=buffer, file_name=filename, mime=mime_type)

    
    
    
# Imports
import streamlit as st
import pandas as pd
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
