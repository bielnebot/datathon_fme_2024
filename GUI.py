import streamlit as st
from PIL import Image
import pandas as pd

from utils.GUI_operations import perform_inference


# Header
st.set_page_config(page_title="Datathon MANGO", page_icon="👗", layout="wide", initial_sidebar_state="expanded")

# Side bar
st.sidebar.image("data/mango-logo.png")
st.sidebar.write("## Instructions:")
st.sidebar.markdown('''
    1. Load an image from the `ìmages` directory
    2. Press on `Inference` to make predictions of the attributes
    ''')

# Main window
st.title("Determining design attributes")
st.write("""### Load an image to identify its attributes""")

# Read csv to retrieve metadata
df = pd.read_csv("data/product_data.csv")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image_name = uploaded_file.name
    # Find the corresponding row in the dataframe
    row = df[df["des_filename"] == image_name]

    image_column, metadata_column = st.columns(2)
    
    with image_column:
        st.write("### 🖼️ Image")
        # Display the image
        image = Image.open(uploaded_file)
        st.image(image, caption=image_name)

    with metadata_column:
        st.write("### 🗒️ Metadata")
        st.dataframe(row.T)

    # Button
    if st.button("Inference"):
        attributes_df = perform_inference(row)
        st.write("## 📊 Predictions")
        st.dataframe(attributes_df)