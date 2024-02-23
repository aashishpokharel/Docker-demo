import os
import re
# import cv2
import time
import warnings
import argparse
import streamlit as st
from PIL import Image, ImageSequence


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'dataset')
UPLOAD_DIR = os.path.join(BASE_DIR, 'dataset', 'uploads')

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)


st.title("Docker Demo")

uploaded_file = st.sidebar.file_uploader("Upload a file", ['jpg', 'png', 'jpeg', 'pdf', 'tif'])
if uploaded_file:
    tif_images = Image.open(uploaded_file)
    st.image(tif_images,  use_column_width=True)           