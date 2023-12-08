import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Firebase 초기화 체크 및 실행
if not firebase_admin._apps:
    
    firebase_config = {
        "type": st.secrets["type"],
        "project_id": st.secrets["project_id"],
        "private_key_id": st.secrets["private_key_id"],
        "private_key": st.secrets["private_key"],
        "client_email": st.secrets["client_email"],
        "client_id": st.secrets["client_id"],
        "auth_uri": st.secrets["auth_uri"],
        "token_uri": st.secrets["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["client_x509_cert_url"]
    }
    
    # cred = credentials.Certificate("./boamong-25709-firebase-adminsdk-szy07-2a5ec92369.json")
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)
# Firestore 인스턴스 생성
db = firestore.client()

def create_idea_page():
    st.header("💡 아이디어를 간략히 소개해 주세요")
    
    st.subheader("아이디어 한줄 소개")
    headliner = st.text_input('아이디어 한줄 소개')
    
    st.subheader("이모지")
    emoji = st.text_input('아이디어를 나타내는 대표 이모지 하나를 입력해주세요!')
    
    st.subheader("What?")
    what = st.text_area('어떤 아이디어인가요?', key = "create_idea_who")
    
    st.subheader("Why?")
    why = st.text_area('왜 이 아이디어를 실행해보면 좋은가요?', key = "create_idea_why")
    
    st.subheader("How?")
    how = st.text_area('대략 어떻게 아이디어를 실행해볼 생각인가요?', key = "create_idea_how")
    
    st.subheader("When?")
    when = st.text_area('아이디어를 실행하는 기간 / 실행을 시작하는 기간은 언제로 예상하나요? 꼭 지금 당장 실행하지 않아도 됩니다', key = "create_idea_when")

    st.subheader("참고 링크")
    link = st.text_input('아이디어를 더 자세히 소개할 수 있는 참고 링크를 첨부해 주세요')
    
    st.subheader("예상 구현 난이도")
    difficulty = st.slider('난이도', 0, 20, key = "create_idea_difficulty")
    st.subheader("아이디아의 파급력 / 임팩트 정도")
    impact = st.slider('임팩트', 0, 20, key = "create_idea_impact")

    if st.button('아이디어 내기'):
        idea_data = {
            "who" : st.session_state['email'],
            "what" : what,
            "why" : why,
            "how" : how,
            "when" : when,
            "link" : link,
            "difficulty" : difficulty,
            "impact" : impact,
            "headliner" : headliner,
            "emoji" : emoji,
            "status" : True,
            'timestamp': datetime.now(),
        }
        
        # Firestore에 데이터 저장 또는 업데이트
        new_doc_ref = db.collection('idea').document()  
        # 생성된 ID를 사용하여 데이터 저장
        new_doc_ref.set(idea_data)
        
        st.success(f'성공적으로 아이디어가 저장되었습니다')