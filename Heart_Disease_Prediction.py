import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

#model = open("models/dt_4.bin", "rb")
pickle_in = open('heart1.pkl','rb')
clf = pickle.load(pickle_in)

def Welcome():
    return 'WELCOME ALL!'

def predict_price(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldspeak,slope,ca,thal):    

    x = np.zeros(22)
    x[0] = age
    x[1] = sex
    x[2] = cp
    x[3] = trestbps
    x[4] = chol
    x[5] = fbs
    x[6] = restecg
    x[7] = thalach
    x[8] = exang
    x[9] = oldspeak
    x[10] = slope
    x[11] = ca
    x[12] = thal

    #if loc_index >= 0:
        #   x[loc_index] = 1

    return clf.predict([x])[0]


def main():
    st.title("Heart Disease Prediction")
    html_temp = """
    <h2 style="color:black;text-align:left;"> Use AI to check your Heart Disease </h2>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.subheader('Please enter the required details:')
    age = st.text_input("Age","")
    sex = st.text_input("Sex: 1 for male and 0 for female","")
    cp  = st.text_input("value of cp","")
    trestbps = st.text_input("Value of trestbps","")
    chol = st.text_input("value of chol","")
    fbs = st.text_input("value of fbs","")
    restecg = st.text_input("Value of restecg","")
    thalach = st.text_input("Value of thalach","")
    exang = st.text_input("Enter the value of exang","")
    oldspeak = st.text_input("Value of oldspeak","")
    slope = st.text_input("Value of Slope","")
    ca = st.text_input("Value of ca","")
    thal = st.text_input("Enter the value of thal","")

    result=""

    if st.button("Predict"):
        result=predict_price(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldspeak,slope,ca,thal)
    st.success('Result {}'.format(result))
    if st.button("About"):
        st.markdown("Please find the GitHub link [here](https://github.com/Lokeshrathi/Bangalore-house-s-rate)")
    
if __name__=='__main__':
    main()
    