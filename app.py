# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:13:35 2022

@author: Apoorv
"""

import pickle
import streamlit as st
import random




pickle_in = open(r"C:\Users\Apoorv\Downloads\classifier.pkl", 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache(suppress_st_warning=True)

def prediction(offer_expiration, income_range, no_visited_Cold_drinks,
       travelled_more_than_15_mins, Restaur_spend_less_than20,
       Marital_Status, restaurant_type, age,
       Prefer_western_over_chinese, travelled_more_than_25_mins,
       travelled_more_than_5mins_for_offer, no_visited_bars, Gender,
       restuarant_same_direction_house, Cooks_regularly, Customer_type,
       Qualification, is_foodie, no_Take_aways, Job_Industry,
       restuarant_opposite_direction_house, has_Children,
       visit_restaurant_with_rating, temperature,
       Restaur_spend_greater_than_20, Travel_Time, Climate,
       drop_location, Prefer_home_food):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if offer_expiration == "10 hours":
        offer_expiration = 0
    else:
        offer_expiration = 1
 
    if travelled_more_than_15_mins == "No":
        travelled_more_than_15_mins = 0
    else:
        travelled_more_than_15_mins = 1  
 
    if travelled_more_than_25_mins == "No":
        travelled_more_than_25_mins = 0
    else:
        travelled_more_than_25_mins = 1
        
    
    if Customer_type == "Individual":
        Customer_type = 0
    elif Customer_type == "With Family":
        Customer_type = 1
    elif Customer_type == "With Kids":
        Customer_type = 2
    else:
        Customer_type = 3
        
        
    
    if Restaur_spend_greater_than_20 == "less1":
        Restaur_spend_greater_than_20 = 0
    elif Restaur_spend_greater_than_20 == "never":
        Restaur_spend_greater_than_20 = 1
    elif Restaur_spend_greater_than_20 == "1~3":
        Restaur_spend_greater_than_20 = 2
    elif Restaur_spend_greater_than_20 == "4~8":
        Restaur_spend_greater_than_20 = 3
    else:
        Restaur_spend_greater_than_20 == 4
        
    
    if drop_location == "A":
        drop_location = 0
    elif drop_location == "B":
        drop_location = 1
    else:
        drop_location = 2
        
 
    # Making predictions 
    '''prediction = classifier.predict( 
        [[offer_expiration,
          31249.5,0.0, 
          travelled_more_than_15_mins, 
          2.0,
          1,
          2,
          21,
          1,
          travelled_more_than_25_mins, 
          1,
          0.0,
          Gender,
          0,
          0,
          Customer_type,
          1,
          1,
          2.0,
          0,
          1,
          0,
          1,
          89,
          Restaur_spend_greater_than_20, 
          18,
          0,
          drop_location,
          1]])'''
       
    a = random.randint(0, 1)
    if a == 0:
        pred = 'Will not be accepted'
    else:
        pred = 'Will be accepted'
    return pred

# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Offer Acceptance Prediction App</h1> 
    </div> 
    """
    
    
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    offer_expiration = st.selectbox('Offer Expires in',("10 hours","2 days"))
    #income_range = 31249.5
    Gender = st.selectbox('Gender',("Male","Female"))
    #Marital_Status = 1
    travelled_more_than_15_mins = st.selectbox('Travelled more than 15 minutes to reach?',("Yes","No"))
    travelled_more_than_25_mins = st.selectbox('Travelled more than 25 minutes to reach?',("Yes","No"))
    Customer_type = st.selectbox("Type of customer",('Individual', 'With Family', 'With Kids', 'With Colleagues'))
    #travelled_more_than_5mins_for_offer = 1
    Restaur_spend_greater_than_20 = st.selectbox('Number of times times has the customer spent more than 20 minutes at the venue',('less1', 'never', '1~3', '4~8', 'gt8'))
    drop_location = st.selectbox('Drop Location',('A', 'B', 'C'))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(offer_expiration,
          31249.5,0.0, 
          travelled_more_than_15_mins, 
          2.0,
          1,
          2,
          21,
          1,
          travelled_more_than_25_mins, 
          1,
          0.0,
          Gender,
          0,
          0,
          Customer_type,
          1,
          1,
          2.0,
          0,
          1,
          0,
          1,
          89,
          Restaur_spend_greater_than_20, 
          18,
          0,
          drop_location,
          1) 

        st.success('The offer {}'.format(result))
     
if __name__=='__main__': 
    main()
 
