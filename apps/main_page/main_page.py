import streamlit as st

def app():
    st.write('👆🏻 🔺 ☝ 네비게이션을 사용하여 페이지를 이동하세요.')
    st.title('What We Achieved')

#     used_car_prediction = '[🚗  차종 분류](https://share.streamlit.io/inwookie/ss501_ai_bootcamp_hackathon/main/app.py)'
#     st.markdown(used_car_prediction, unsafe_allow_html=True)
    st.markdown("""
    ### 🚗  차종 분류 
    ### 🚓  번호판 인식  
    ### 🚐  파손 인식  
    ### 🚙  중고차 가격 예측   
    """)
