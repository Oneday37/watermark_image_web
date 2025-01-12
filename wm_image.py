import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


st.title("Watermark Image")
st.header("Watermark your JPG, PNG, and JPEG Image")

# UPLOAG GAMBAR ASLI
uploaded_image_text = st.file_uploader(
    "Upload gambar yang ingin anda berikan watermark (.JPG, .PNG, .JPEG):", type=["png", "jpg", "jpeg"], key="text_upload"
)

if uploaded_image_text:
    # MEMBUKA GAMBAR YANG TELAH DIUPLOAD
    main_image_text = Image.open(uploaded_image_text).convert("RGBA")

    # MENAMPILKAN GAMBAR YANG TELAH DIUPLOAD
    st.image(main_image_text, caption="Gambar yang Diupload",
             use_container_width=True)

    # MEMBUAT SALINAN GAMBAR
    copied_image_text = main_image_text.copy()
    draw = ImageDraw.Draw(copied_image_text)

    # KONFIGURASI WATERMARK TEXT
    watermark_text = "Watermark Image"
    font_size = 80
    font = ImageFont.truetype("arial.ttf", font_size)

    # MENGHITUNG AREA DARI WATERMARK TEXT
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_fill = (255, 255, 255, 128)  # WARNA WATERMARK TEXT

    # JARAK ANTAR WATERMARK TEXT
    gap = 40

    # LOOPING WATERMARK TEXT
    for y in range(0, copied_image_text.height, text_height + 30):
        for x in range(0, copied_image_text.width, text_width + gap):
            draw.text((x, y), watermark_text, font=font, fill=text_fill)

    # MENAMPILKAN GAMBAR YANG TELAH DIBERIKAN WATERMARK
    st.image(copied_image_text, caption="Gambar dengan Watermark",
             use_container_width=True)
