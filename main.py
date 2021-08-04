import streamlit as st
from vietnam_number import n2w
import re
from docx import Document
uploaded_file = st.file_uploader("Upload Files",type=['docx'])
from vietTTS.synthesizer import TextToSpeech
text = "324 43/32"
text = re.sub(r"(\d+)", lambda x: n2w(x.group(0)), text)
print(text)
textToSpeech = TextToSpeech()

if uploaded_file is not None:
    doc = Document(uploaded_file)
    
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    m = " "
    output = "clip/clip_test.wav"
    result = []
    for paragraph in doc.paragraphs:
        if 'Heading' in paragraph.style.name:
            m = re.sub(r"(\d+)", lambda x: n2w(x.group(0)), m)
            textToSpeech.return_clip(m,output)
            m = ""
            m =m + paragraph.text
            st.write(output)
            st.audio(output)
            output = "clip/clip_{}.wav".format(" ".join(paragraph.text.split(" ")[0:2]))
        else:
            m = m + paragraph.text
    textToSpeech.return_clip(m,output)
