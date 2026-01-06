import streamlit as st
import pandas as pd
import numpy as np

#페이지 기본설정
st.set_page_config(layout="wide", page_title="나만의 포트폴리오")
st.set_page_icon="📈"
st.title("🚀 매출 데이터 분석 리포트")
st.markdown("---")

# [사이드바 처리 로직]
with st.sidebar:
    st.header("설정")
    uploaded_file = st.file_uploader("csv 파일 업로드", type=['csv'])
    
    chart_type = st.selectbox("차트 종류 선택", ["Line Chart", "Bar Chart", "Area Chart"])
    
    count = st.selectbox("데이터 미리보기 개수", options=[5,10,15,20,25,30,35,40,45,50], index=1)
    
# [메인 데이터 처리 로직]

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.success("파일 업로드 성공")
    
else:
    #실습용 더미 데이터 (파일이 없을 경우)
    st.info ("데이터가 없을 경우, 이 파일로 실행됩니다.")
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A','B','C']
    )
    
# [레이아웃] 다중 컬럽으로 화면 분할
col1, col2 = st.columns(2)

with col1:
    st.subheader("데이터 미리보기")
    st.dataframe(df.head(count))
    
with col2:
    st.subheader("데이터 시각화")
    if chart_type == "Line Chart":
        st.line_chart(df)
    if chart_type == "Bar Chart":
        st.bar_chart(df)
    elif chart_type =="Area Chart":
        st.area_chart(df)
        
#통계 요약
with st.expander("기초 통계 확인하기"):
    st.subheader("📊 데이터 기초 통계 분석")
    st.write("연구실 실험 데이터의 평균, 표준편차 등을 확인합니다.")
    st.write(df.describe())