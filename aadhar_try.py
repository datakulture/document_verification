
#import cv2
import streamlit as st

#from io import StringIO 
#import cv2
#import matplotlib.pyplot as plt
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  #this line is not needed in hosted app
#from pytesseract import Output
import re
#import numpy as np
from PIL import Image


#adding a file uploader
st.title("Aadhar number extractor")
st.write("Optical Character Recognition (OCR) implementation in Python")
        
file = st.file_uploader("Please choose a file", type=["png","jpg"])

if file is not None:
    img = Image.open(file)
    #img = cv2.imread(img)
    custom_config = r'--psm 6'
    text1 = pytesseract.image_to_string(img, lang = 'eng+tam', config= custom_config).upper().replace(" ", "")
    number = str(re.findall(r"[0-9]{11,12}", text1)).replace("]", "").replace("[","").replace("'", "")
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("The Aadhar number is")
    number

