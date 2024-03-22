from PIL import Image
import streamlit as st

from rembg import remove

from utils import crop, prepare_to_save

def main():
    """Program takes an image, removes background and crops empty edges"""

    st.set_page_config(page_title="Удалятор 3000", layout="wide", page_icon=":robot_face:")

    st.sidebar.write("Загрузить и сохранить :gear:")

    upload = st.sidebar.file_uploader("Выберите изображение", type=["jpg", "png"], accept_multiple_files=False)

    # if some image uploaded do logic on that image, else use default image
    if upload:
        img_name = upload.name
        img = Image.open(upload)
        remove_and_crop(img, img_name)
    else:
        img = Image.open("data/cat.jpg")
        remove_and_crop(img, "cat.jpg")
        

def remove_and_crop(img, img_name):
    """Makes 3 columns with original image, no background image and cropped image.
    Adds buttons to download results"""

    col1, col2, col3 = st.columns(3)

    # Displays original image
    col1.image(img, "Исходное изображение")

    # Shows spinner while background removing, then displays new image
    with st.spinner(":scissors: удалаем фон..."):
        no_bg = remove(img)
    col2.image(no_bg, "Изображение без фона")

    # Shows spinner while cropping, then displays new image
    with st.spinner(":scissors: обрезаем края..."):
        cropped = crop(no_bg)
    col3.image(cropped, "Обрезанное изображение")

    # Adds no background image download button
    st.sidebar.download_button(
        label="Скачать без фона",
        data=prepare_to_save(no_bg),
        file_name="no_bg_" + img_name,
        mime="image/png",
    )

    # Adds cropped image download button
    st.sidebar.download_button(
        label="Скачать обрезанное",
        data=prepare_to_save(cropped),
        file_name="cropped_" + img_name,
        mime="image/png",
    )

if __name__ == "__main__":
    main()