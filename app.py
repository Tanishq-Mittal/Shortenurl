import streamlit as st
import qrcode
import pyshorteners
from io import BytesIO

st.set_page_config(page_title="Premium QR Generator")

st.title("🚀 Premium QR Generator")

url = st.text_input("Enter URL")

shorten = st.checkbox("Shorten URL")

if st.button("Generate QR"):

    if not url:
        st.error("Please enter a URL")
        st.stop()

    final_url = url

    if shorten:
        try:
            shortener = pyshorteners.Shortener()
            final_url = shortener.tinyurl.short(url)
            st.success(f"Short URL: {final_url}")
        except:
            st.warning("URL shortening failed. Using original URL.")

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(final_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")

    st.image(buffer.getvalue(), caption="Generated QR Code")

    st.download_button(
        label="📥 Download QR",
        data=buffer.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )
