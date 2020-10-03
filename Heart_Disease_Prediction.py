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
    #st.image('/home/lokesh/Desktop/Projects/Heart_ML_App/Deploying-a-Machine-Learning-Model/images.jpeg')
    st.title("Heart Disease Prediction")
    html_temp = """
    <h2 style="color:black;text-align:left;"></h2>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.sidebar.markdown('**Age**- in years')
    st.sidebar.markdown('**Sex**-(1 = male; 0 = female)')
    st.sidebar.markdown('**CP**- chest pain type')
    st.sidebar.markdown('**trestbps**- resting blood pressure (in mm Hg on admission to the hospital)')
    st.sidebar.markdown('**chol**-serum cholestoral in mg/dl')
    st.sidebar.markdown('**fbs**-(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)')
    st.sidebar.markdown('**restecg**-resting electrocardiographic results')
    st.sidebar.markdown('**thalach**-maximum heart rate achieved')
    st.sidebar.markdown('**oldpeak**-ST depression induced by exercise relative to rest')
    st.sidebar.markdown('**slope**-the slope of the peak exercise ST segment')
    st.sidebar.markdown('**CA**-number of major vessels (0-3) colored by flourosopy')
    st.sidebar.markdown('**thal**- 3 = normal; 6 = fixed defect; 7 = reversable defect')


    #st.balloons() displays Balloons after every 'Enter' pressed

    ## Display Columns
    st.subheader('Please Enter the Required Details:')
    age = st.number_input("Age", min_value=10, max_value=90)
    sex = st.number_input("Sex: Enter 1 for Male and 0 for Female", step=1, min_value=0, max_value=1,value=1)
    cp  = st.number_input("CP:",step=1, min_value=0, max_value=3,value=1)
    trestbps = st.text_input("Value of trestbps","")
    chol = st.text_input("Value of chol","")
    fbs = st.number_input("Value of fbs-(fasting blood sugar > 120 mg/dl)",step=1, min_value=0, max_value=1,value=1)
    restecg = st.number_input("Resting electrocardiographic results(restecg)",step=1, min_value=0, max_value=2,value=1)
    thalach = st.text_input("Value of Thalach - Maximum Heart Rate Achieved","")
    exang = st.number_input("exang-exercise induced angina",step=1, min_value=0, max_value=1,value=1)
    oldspeak = st.number_input("Value of oldspeak",step=0.1, min_value=0.0, max_value=4.0,value=0.0)
    slope = st.number_input("Value of Slope",step=1, min_value=0, max_value=2,value=1)
    ca = st.number_input("Value of ca",step=1, min_value=0, max_value=4,value=1)
    thal = st.number_input("Value of thal",step=1, min_value=0, max_value=3,value=1)

    result=""

    if st.button("Predict"):
        result=predict_price(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldspeak,slope,ca,thal)
    st.success('Your Results {} '.format(result))
    st.markdown('1 - Diseased, 0 - Not Diseased')
    if st.button("About"):
        st.markdown("Please find the Code using my [GitHub link] (https://github.com/Lokeshrathi/Deploying-a-Machine-Learning-Model)")
    
    page_bg_img = '''
    <style>
    body {
         background-image: url("");
        background-size: cover;
        background-color:white;
        }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

if __name__=='__main__':
    main()
    