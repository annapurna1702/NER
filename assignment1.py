import streamlit as st
import spacy
from spacy import displacy

import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from newspaper import Article


st.title("Named Entity Recognition")
url=st.text_input("Enter URL :")
para=st.text_area("Or, enter your own paragraph :")



if st.button("Analyze"):
   if (url):
      article=Article(url)
      article.download()
      article.parse()
      doc=nlp(article.text)
      ent_html=displacy.render(doc,jupyter=False,style='ent')
      st.markdown(ent_html, unsafe_allow_html=True)
   elif (para):
      doc=nlp(para)
      ent_html=displacy.render(doc,jupyter=False,style='ent')
      st.markdown(ent_html, unsafe_allow_html=True)
   
   else:
      st.text("Sorry, you have entered nothing! Please try again")
    
      
