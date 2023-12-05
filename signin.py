import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore

# Firebase 초기화
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

db = firestore.client()

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'email' not in st.session_state:
    st.session_state['email'] = None

# def set_local_storage():
#     # localStorage에 loggedIn을 True로 설정하는 자바스크립트 코드
#     js = """
#         <script>
#         localStorage.setItem('loggedIn', 'True');
#         </script>
#     """
#     components.html(js, height=0, width=0)
            
def show_signin_page():
    st.header("보아몽 공작소🔨🎨🐘💭")
    st.header("로그인")

    email = st.text_input('Email', key='signin_email')

    st.caption("로그인 버튼을 눌러주세요")
    if st.button('로그인'):
        verify, email = verify_user(email)
        if verify:
            # 로그인 성공, app.py로 라우팅
            st.session_state['logged_in'] = True
            # set_local_storage()
            st.session_state['current_page'] = 'app'
            st.session_state['email'] = email
            st.rerun()
        else:
            st.error('잘못된 이메일 혹은 존재하지 않는 이메일입니다')
    
    st.caption("아직 보아몽 공작소 회원이 아니신가요?")
    if st.button('회원가입'):
        # 회원가입 페이지 또는 양식 표시
        st.session_state['current_page'] = 'signup'
        st.rerun()

def verify_user(email):
    profiles = db.collection('profile').where('email', '==', email).stream()
    for profile in profiles:
        profile_data = profile.to_dict()  # profile 객체를 딕셔너리로 변환
        if profile_data.get('email') == email:  # email 필드 확인
            print(profile_data.get('email'))
            return True, profile_data.get('email')
    return False, None