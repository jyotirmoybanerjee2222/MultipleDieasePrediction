# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:47:07 2024

@author: jtrmb
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading savedModel
diabetes_model = pickle.load(open('D:/Multiple Diease prediction/SavedModels/diabetes_model.sav','rb'))
heart_diease_model = pickle.load(open('D:/Multiple Diease prediction/SavedModels/heart_disease_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Multiple Diease Prediction',
                           ['Diabetics Diease predsiction','Heart Diease prediction'],
                           icons = ['activity','heart'],
                           default_index = 0)
    
#diabetic prediction page
if(selected == 'Diabetics Diease predsiction'):
    # page title 
    st.title('Diabetics Diease predsiction Using ML')
    


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')
    
    ##Pregnancies = st.text_input('Number of Pregnancies')
   ## Glucose = st.text_input('Glucose Level')
   ## BloodPressure = st.text_input('Blood Pressure value')
    ##SkinThickness = st.text_input('Skin Thickness value')
    ##Insulin = st.text_input('Insulin Level')
    ##BMI = st.text_input('BMI value')
    ##DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    ##Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_dianosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if(diab_prediction[0]==1):
            diab_dianosis="The person is diabetic"
        else:
            diab_dianosis="The person is  not diabetic"
        st.success(diab_dianosis)
            
        
#Heart Diease prediction   
if(selected == 'Heart Diease prediction'):
    # page title 
    st.title('Heart Diease prediction Using ML')
    


    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
