
import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="EV Battery Early Warning System",
    page_icon="🔋",
    layout="wide"
)

st.title("🔋 AI-Based EV Battery Early-Warning System")
st.write(
    "This prototype analyses battery experiment data "
    "to explore abnormal temperature and mechanical behaviour."
)

st.warning(
    "Research prototype only. This application is not a "
    "certified thermal-runaway detection or safety system."
)

st.header("1. Load your dataset")

temperature_file = st.file_uploader(
    "Upload M2_Temperature.csv",
    type=["csv"]
)

force_file = st.file_uploader(
    "Upload M2_Force.csv",
    type=["csv"]
)


def inspect_file(uploaded_file, title):
    if uploaded_file is None:
        st.info(f"Please upload {title}.")
        return

    try:
        df = pd.read_csv(uploaded_file)

        st.subheader(title)
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        st.write("Column names:")
        st.write(list(df.columns))

        st.write("First 10 rows:")
        st.dataframe(df.head(10), use_container_width=True)

        st.write("Missing values:")
        st.dataframe(
            df.isnull().sum().rename("Missing values")
        )

        return df

    except Exception as error:
        st.error(f"Could not read the CSV: {error}")
        return None


temperature_df = inspect_file(
    temperature_file, "Temperature Data"
)

force_df = inspect_file(
    force_file, "Force Data"
)

if temperature_df is not None and force_df is not None:
    st.success("Both files loaded. Review their columns before modelling.")

st.header("2. Next development steps")
st.write("""
- Verify the measurement columns and units.
- Identify the experimental timeline and event labels.
- Prepare the data for analysis.
- Train and evaluate an appropriate AI anomaly-detection model.
- Add alerts and visualisations after validating the data.
""")
