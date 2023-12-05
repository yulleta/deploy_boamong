import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import streamlit as st

# Firebase 초기화 체크 및 실행
if not firebase_admin._apps:
    # cred = credentials.Certificate("./boamong-25709-firebase-adminsdk-szy07-2a5ec92369.json")
    cred = credentials.Certificate(st.secrets['json'])
    firebase_admin.initialize_app(cred)
# Firestore 인스턴스 생성
db = firestore.client()

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'signin'
    

def show_signup_page():
    st.header("회원가입")
    st.caption("새로고침을 하면 로그인 화면으로 넘어갑니다")

    # 회원가입 양식 필드
    email = st.text_input('Email (Signup)', key='signup_email')  
    name = st.text_input('이름', key='signup_name')
    year = st.number_input('기수', min_value=1, key='signup_year')
    interest= ["없음"]
    career = ["없음"]
    introduction = "한줄 소개"
    link = "자기소개 링크"
    visual_conf = 0
    analy_conf = 0
    engin_conf = 0
    program_conf = 0
    visual_stacks = ['없음']
    analy_stacks = ['없음']
    engin_stacks = ['없음']
    program_stacks = ['없음']
    bookmark = []
    on_process = []
    
    # 추가 필요한 필드를 여기에 구현

    if st.button('Create Account'):
        # Save button
        verify_email = db.collection('profile').where('email', '==', email).stream()
        if ('@' not in email):
            st.error('메일 형식이 잘못되었습니다.')    
        elif any(verify_email):
            st.error('이미 가입된 회원입니다.')
        else:
            # 새로운 회원 생성
            profile_data = {
                "name": name,
                "year": year,
                "email": email,
                "interest": interest,
                "career" : career,
                "introduction" : introduction,
                "link" : link,
                "visual_conf" : visual_conf,
                "analy_conf" : analy_conf,
                "engin_conf" : engin_conf,
                "program_conf" : program_conf,
                "visual_stacks" : visual_stacks,
                "analy_stacks" : analy_stacks,
                "engin_stacks" : engin_stacks,
                "program_stacks": program_stacks,
                "bookmark" : bookmark,
                "on_process" : on_process,
            }
            new_doc_ref = db.collection('profile').document()
            new_doc_ref.set(profile_data)
            st.toast("성공적으로 회원 가입이 되었습니다")
            st.session_state['signed_up'] = True
            st.rerun()