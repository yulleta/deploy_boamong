import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import streamlit as st
from streamlit_option_menu import option_menu

from signin import show_signin_page
from signup import show_signup_page
from user_modify import modify_user_page
from user_show import show_user_page
from idea import create_idea_page
from idea_plot import show_idea_plot
from ppl_plot import show_ppl_plot
from info import show_info_page

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
# Firestore 인스턴스 생성
db = firestore.client()

# 자바스크립트로 로그인 상태 확인 및 Streamlit 세션 상태에 저장
# def check_login_status():
#     st.markdown("""
#         <script>
#         const loggedIn = localStorage.getItem("loggedIn"); // 또는 쿠키에서 읽기
#         if (loggedIn) {
#             window.parent.postMessage({
#                 type: 'streamlit:setComponentValue',
#                 key: 'loggedIn',
#                 value: true
#             }, '*');
#         }
#         </script>
#     """, unsafe_allow_html=True)

# print(check_login_status())

# 로그인 상태 확인
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    
    # current_page, signed_up, profile_modify 초기화
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'signin'
    if 'signed_up' not in st.session_state:
        st.session_state['signed_up'] = False
        
    if 'profile_modify' not in st.session_state: 
        st.session_state['profile_modify'] = "read"
    if 'idea_modify' not in st.session_state: 
        st.session_state['idea_modify'] = "read"
        
    if 'profiles_search_stack' not in st.session_state:
        st.session_state['profiles_search_stack'] = []
    if 'profiles_search_conf' not in st.session_state:
        st.session_state['profiles_search_conf'] = []
    if 'profiles_search_interest' not in st.session_state:
        st.session_state['profiles_search_interest'] = []
    if 'profiles_search_career' not in st.session_state: 
        st.session_state['profiles_search_career'] = []
    
    # 회원가입 후 로그인 페이지로 리디렉션
    if 'signed_up' in st.session_state and st.session_state['signed_up']:
        st.session_state['current_page'] = 'signin'

    if st.session_state['current_page'] == 'signup':
        show_signup_page()
    if st.session_state['current_page'] == 'signin':
        show_signin_page()
    
else:
    # 페이지 네비게이션
    with st.sidebar:
        page = option_menu("보아몽 공작소", ["보아몽 공작소?", "마이페이지", "idea 등록", "idea 목록", "사람 찾기"],
                            icons=['info-circle', 'person', 'lightbulb', 'card-list', 'compass'],
                            menu_icon="magic", default_index=0,
                            styles={
            "container": {"padding": "4!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
            "nav-link-selected": {"background-color": "#c5a6ff"},
        }
        )
        
        st.caption("F5키를 누르거나 새로고침을 하면 로그인 화면으로 돌아갑니다")
        st.caption("사이트 개발자/소모임 부장 : 21기 분석 김민경")
    
    if page == "보아몽 공작소?":
        show_info_page()
    elif page == "마이페이지":
        if st.session_state['profile_modify'] == "read":
            show_user_page()
        else:
            modify_user_page()
    elif page == "idea 등록":
        create_idea_page()
    elif page == "idea 목록":
        show_idea_plot()
    elif page == "사람 찾기":
        show_ppl_plot()


