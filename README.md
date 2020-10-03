# Deploying-a-Machine-Learning-Model

## Inspiration
### Want to learn how to Deploy your model on Ubuntu using Streamlit on Heroku, you are at the correct place.

## Data:
- Collected from [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci)

### Data Columns:
- age
- sex
- chest pain type (4 values)
- resting blood pressure
- serum cholestoral in mg/dl
- fasting blood sugar > 120 mg/dl
- resting electrocardiographic results (values 0,1,2)
- maximum heart rate achieved
- exercise induced angina
- oldpeak = ST depression induced by exercise relative to rest
- the slope of the peak exercise ST segment
- number of major vessels (0-3) colored by flourosopy
- thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

## Work:
- Need to predict if a person has Heart Disease or not.

## SuperVised Learning:
- Used Logistic Regression with Hyperparameter Tuning to obtain 87% accuracy and **96% Recall Value for the case.**

## Deployment:
- Used Streamlit to create the Web Application.
- Used Heroku platform for deployment my Web Application.

### Notes:
- Learnt about using the version during Local Deployment. 
_ Keep in mind to deploy the model using the same local environment as it was trained on. (I previously did the mistake of modelling at Kaggle and then using the saved model to deploy on my localhost).
- Use the [Streamlit Cheat Sheet](https://discuss.streamlit.io/t/streamlit-cheat-sheet/4912) while coding.
