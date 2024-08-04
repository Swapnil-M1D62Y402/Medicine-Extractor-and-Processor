from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image 
import google.generativeai as genai

load_dotenv() #load all the env vars from .env

#configure the genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_CONFIG = {
    "temperature": 0.2,     #to keep the generation low
    "top_p":1,
    "top_k":32,
    "max_output_tokens": 4096,
}

#convert image file to stream of bytes 
def convert_img_to_byte_dict(uploaded_file):
    if uploaded_file is not None:
        #read file into byte 
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": "image/png", 
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File not Uploaded")
    
def genai_response(sys_prompt, uploaded_file, prompt):
    #function to load Gemini Pro Vision 
    model = genai.GenerativeModel(model_name='gemini-1.5-flash',
                                  generation_config=MODEL_CONFIG)
    image_info = convert_img_to_byte_dict(uploaded_file)
    #response = model.generate_content([sys_prompt, image[0], prompt])
    response = model.generate_content([sys_prompt, image_info[0], prompt])
    return response.text


#intializing streamlit app 

st.set_page_config(page_title="Multilanguage Text Extractor")

css = """
<style>
body {
    background-color: #00008B;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

st.title("Medical Text Extractor")
st.header("Gemini API Application")

input=st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an Image of the Invoice...", type=["jpg", "jpeg", "png"])

image=""

if uploaded_file is not None:
    image=Image.open(uploaded_file)  #initially it is empty, if uploaded then fill it
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit=st.button("Tell me about the invoice")


sys_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices and
you will have to answer questions based on the input image
"""

#if submit button is clicked
if submit:
    response=genai_response(sys_prompt,uploaded_file, input)
    st.subheader("Response : ")
    st.write(response)


### Detection of drugs in the text 

from drug_named_entity_recognition import find_drugs

drugs = find_drugs(response.split(" "), is_ignore_case=True)


import json

def print_medication_name(data):
  """Prints the name of a specific medication from the JSON data.

  Args:
    data: The JSON data.
    index: The index of the medication to print (starting from 0).
  """
  for key, value in data:
    if key == "medicine":
        st.subheader("Specifically Medicine Name: ")
        st.write(value)


#print_medication_name(response)

st.subheader("Medicines listed : ")
st.write(drugs)

