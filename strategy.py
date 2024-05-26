
import streamlit  as st
import joblib
import pandas as pd
import sklearn 

model = joblib.load('strategy.h5')
Inputs = joblib.load('input_strategy.h5')

def predict(interest_rate,credit,march,may,previous,duration) :
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0,'interest_rate'] = interest_rate
    test_df.at[0,'credit'] = credit
    test_df.at[0,"march"] = march
    test_df.at[0,"may"] = may
    test_df.at[0,"previous"] = previous
    test_df.at[0,"duration"] = duration
    result = model.predict(test_df)[0]
    return result

def main () :
    st.title('Test your strategy') 
    interest_rate = st.slider("interest_rate" , min_value=10 , max_value=90 , value=25 , step=1)
    credit = st.selectbox("credit" ,[0, 1])
    march = st.slider("march" , min_value=0.0 , max_value= 200.0 , value=25.0 , step=0.2)
    may = st.slider("may" , min_value=0.0 , max_value=110.0 , value=25.0 , step=0.2)
    previous = st.slider("previous" , min_value=0.0 , max_value=180.0 , value=25.0 , step=0.2)
    duration = st.slider("duration" , min_value=0.0 , max_value=110.0 , value=25.0 , step=0.2)

    
    if st.button('Predict') :
        result = predict(interest_rate,credit,march,may,previous,duration)
        if resule == 0 :
            st.write('your strategy level is {} which means it might not be successful'.format(result))
        else : 
            st.write('your strategy level is {} which means it might be successful'.format(result))           

        
        
if __name__ == '__main__' :
    main()
