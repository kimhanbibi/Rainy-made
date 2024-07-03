
import streamlit as st
import pandas as pd
import numpy as np

#타이틀
st.title("이것은 타이틀입니다")

#특수이모티콘 예시
st.title('스마일 :sunglasses:')

st.title('스마일 :sunglasses:')

#캡션 넣기
st.caption('캡션을 한번 넣어봤습니다')

#코드 표시
sample_code='''
def fuction():
ptint("hello world")
'''
st.code(sample_code , language="python")

#마크문법
#컬러코드 - blue , green , orange, red , violet
st.markdown("텍스트의 색상을:green[초록색]으로, 그리고**:blue[파란색]**볼트체로 설정할수있다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$]와 같이 latex 문법의 수식도 표현 가능합니다:pencil:")

#라텍스 수식지원 -라텍스는 수식과 같은 과학기호들을 화면에 표시할수있다
st.latex(r'\sqrt{x^2+y^2}=1')
