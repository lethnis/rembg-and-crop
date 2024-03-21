from PIL import Image
import streamlit as st

from rembg import remove

from utils import crop, prepare_to_save

st.set_page_config(page_title="Remover", layout="wide", page_icon=":gem:")

st.sidebar.write("Upload and download :gear:")

img = st.sidebar.file_uploader("Pick an image", type=["jpg", "png"], accept_multiple_files=False)

col1, col2, col3 = st.columns(3)


if img:
    img_name = img.name
    img = Image.open(img)
    col1.image(img, "Base image")

    with st.spinner("Removing background :scissors:..."):
        no_bg = remove(img)
    col2.image(no_bg, "Image with no background")

    with st.spinner("Cropping empty edges :scissors:..."):
        cropped = crop(no_bg)
    col3.image(cropped, "Cropped image")

    st.sidebar.download_button(
        label="Download without background",
        data=prepare_to_save(no_bg),
        file_name="no_bg_" + img_name,
        mime="image/png",
    )

    st.sidebar.download_button(
        label="Download cropped",
        data=prepare_to_save(cropped),
        file_name="cropped_" + img_name,
        mime="image/png",
    )
