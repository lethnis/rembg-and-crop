from io import BytesIO
from PIL import Image
import streamlit as st

from rembg import remove

from utils import crop

st.set_page_config(page_title="Remover", layout="wide")

st.sidebar.write("Upload and download :gear:")

img_file = st.sidebar.file_uploader("Pick an image", type=["jpg", "png"], accept_multiple_files=False)

col1, col2, col3 = st.columns(3)


if img_file:
    img = Image.open(img_file)
    col1.image(img, "Base image")

    with st.spinner("Removing background..."):
        no_bg = remove(img)
    col2.image(no_bg, "Image with no background")

    with st.spinner("Cropping empty edges..."):
        cropped = crop(no_bg)
    col3.image(cropped, "Cropped image")

    buf = BytesIO()
    cropped.save(buf, format="PNG")
    img_io = buf.getvalue()
    st.sidebar.download_button("Download cropped", img_io, "output.png", "image/png")
