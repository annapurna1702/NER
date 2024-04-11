#!/bin/bash

# Update package lists
sudo apt-get update

# Install Python and pip
sudo apt-get install python3 python3-pip -y

# Install spaCy and its language models
pip install spacy
python -m spacy download en_core_web_sm

# Install other dependencies specified in requirements.txt
pip install -r requirements.txt

# Run the Streamlit app
streamlit run assignment1.py

