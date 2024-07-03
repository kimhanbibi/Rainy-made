import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello, Streamlit!')
st.write('Welcome to your first Streamlit app.')

# 간단한 데이터 입력 예제
user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello, {user_input}!")

#data frame 생성
#data frame=pd.DataFrame({'first column':{1,2,3,4},
 #                        'second column':{10,20,30,40},
   #                      })

data_frame = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

#use_container_width 기능은 데이터 프레임을 컨테이너 크기에 확장할때 사용합니다(true/False)                    
st.write(data_frame,use_container_width=False)

# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
st.table(data_frame)

# DataFrame
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)
st.dataframe(data_frame, use_container_width=False)


# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
st.table(data_frame)


# # 메트릭
st.metric(label="온도", value="10°C", delta="1.2°C")
st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

# 컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,300 원", delta="-11.50 원")
col2.metric(label="일본JPY(100엔)", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")