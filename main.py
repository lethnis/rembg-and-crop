from PIL import Image
import streamlit as st

from rembg import remove

from utils import crop

st.set_page_config(page_title="Remover", layout="wide")

col1, col2, col3 = st.columns(3)

img = col1.file_uploader("Pick an image", type=["jpg", "png"], accept_multiple_files=False)


if img:
    img = Image.open(img)
    col1.image(img, "Base image")

    with st.spinner("Removing background..."):
        no_bg = remove(img)
    col2.image(no_bg, "Image with no background")
    
    with st.spinner("Cropping empty edges..."):
        cropped = crop(no_bg)
    col3.image(cropped, "Cropped image")
