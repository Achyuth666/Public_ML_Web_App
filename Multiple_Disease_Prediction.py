# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 21:18:50 2025

@author: Achyu
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models:
diabetes_model = pickle.load(open('C:/Users/Achyu/OneDrive/Desktop/Coding/Machine Learning/Model Deployment/Diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/Achyu/OneDrive/Desktop/Coding/Machine Learning/Model Deployment/Heart_Disease.sav', 'rb'))

parkinsons_disease_model = pickle.load(open('C:/Users/Achyu/OneDrive/Desktop/Coding/Machine Learning/Model Deployment/Parkinsons_disease.sav', 'rb'))


# creating sidebars for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction', 
                            'Heart Disease Prediction',
                            'Parkinsons disease'],
                           
                           icons=['activity', 'heart', 'person'],
                           
                           default_index=0)

# Diabetes Prediction Page:
if (selected == 'Diabetes Prediction'):
    
    #title:
    st.title("Diabetes Prediction")
        
    
    #getting the input data from the user
    #coloumns for input data
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Blood Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure level')
    with col1:
        SkinThickness = st.text_input('Thickness of skin')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age')   


    #code for prediction
    diab_diagnosis = ''
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if(diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Healty'
    st.success(diab_diagnosis)
    
    
    
    
    
if (selected == 'Heart Disease Prediction'):
    
    #title:
        st.title("Heart Disease Prediction")
    
    
if (selected == 'Parkinsons disease'):
    
    #title:
    st.title("Parkinson Disease Prediction")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    