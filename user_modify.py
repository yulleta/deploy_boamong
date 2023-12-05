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

def modify_user_page(): 
    
    profiles = db.collection('profile').where('email', '==', st.session_state['email']).stream()

    for profile in profiles:
        profile_data = profile.to_dict()
        if profile_data.get('email') == st.session_state['email']:

            interest_options = ["없음", "스포츠⚽", "예술(문화활동)🎨" , "과학기술🧪🔨", "여행🧳", "맛집🍽", "건강💪", "경제💸", "사회🌐"]
            career_options = ['없음', '데이터 분석/시각화', '데이터 과학/ML/DL', '데이터 엔지니어링','프론트엔드', '백엔드','앱개발', '마케팅', '보안']

            visual_stack_options = ['없음', 'googleDataStudio', 'powerBI', 'Tableau']
            analy_stack_options = ['없음', '시계열', '컴퓨터 비전(CV)', '멀티모달(multi-modal)', '자연어처리(NLP)', '강화학습(RL)', '추천시스템(RS)', 'pytorch', 'R', 'tensorflow']
            engin_stack_options = ['없음', 'apache airflow', 'apache flink', 'apche hadoop', 'apache kafka', 'apache spark', 'apache storm',\
                'aws', 'azure', 'docker', 'gcp', 'googlebigquery', 'kubernets', 'mongodb', 'mysql', 'postgresql', 'snowflake']
            program_stack_options = ['없음', 'React.js', 'Vue.js', 'streamlit', 'swift', 'android', 'react native', 'spring', 'node.js', 'flask', 'django', 'unity', 'unreal']
            
            # Profile fields
            name = st.text_input('이름', key = "user_modify_name", value = profile_data.get('name'))
            year = st.number_input('기수', min_value=1, key = "user_modify_year", value = profile_data.get('year'))
            interest = st.multiselect('관심분야', options=interest_options, key = "user_modify_interest", default=profile_data.get('interest'))  # interest_options는 관심사 목록
            career = st.multiselect('희망진로', options=career_options, key = "user_modify_career", default=profile_data.get('career'))  # career_options는 경력 목록
            introduction = st.text_input('한줄 자기소개', key = "user_modify_introduction", value=profile_data.get('introduction'))
            link = st.text_input('자기소개 링크 / 연락처', key = "user_link", value=profile_data.get('link'))

            # Confidence levels
            visual_conf = st.slider('Visual Confidence', 0, 10, key = "user_modify_visual_conf", value = profile_data.get('visual_conf'))
            analy_conf = st.slider('Analytical Confidence', 0, 10, key = "user_modify_analy_conf", value = profile_data.get('analy_conf'))
            engin_conf = st.slider('Engineering Confidence', 0, 10, key = "user_engin_conf", value = profile_data.get('engin_conf'))
            program_conf = st.slider('Programming Confidence', 0, 10, key = "user_program_conf", value = profile_data.get('program_conf'))
            
            # Stacks
            visual_stacks = st.multiselect('Visual Stacks', options=visual_stack_options, key = "user_modify_visual_stacks", default=profile_data.get('visual_stacks'))
            analy_stacks = st.multiselect('Analytical Stacks', options=analy_stack_options, key = "user_modify_analy_stacks", default=profile_data.get('analy_stacks'))
            engin_stacks = st.multiselect('Engineering Stacks', options=engin_stack_options, key = "user_modify_engin_stacks", default=profile_data.get('engin_stacks'))
            program_stacks = st.multiselect('Programming Stacks', options=program_stack_options, key = "user_modify_program_stacks", default=profile_data.get('program_stacks'))
            
            # Save button
            if st.button('Update Profile'):
                # 사용자 이메일로 프로필 문서 검색
                profiles = db.collection('profile').where('email', '==', st.session_state['email']).stream()

                profile_found = False
                for profile in profiles:
                    profile_data = profile.to_dict()
                    if profile_data.get('email') == st.session_state['email']:
                        # 업데이트할 새 프로필 데이터
                        updated_data = {
                            "name": name,
                            "year": year,
                            "interest": interest,
                            "career": career,
                            "introduction": introduction,
                            "link": link,
                            "visual_conf": visual_conf,
                            "analy_conf": analy_conf,
                            "engin_conf": engin_conf,
                            "program_conf" : program_conf,
                            "visual_stacks": visual_stacks,
                            "analy_stacks": analy_stacks,
                            "engin_stacks": engin_stacks,
                            "program_stacks" : program_stacks
                        }

                        # 해당 문서 업데이트
                        db.collection('profile').document(profile.id).set(updated_data, merge=True)
                        st.session_state['profile_modify'] = "read"
                        profile_found = True
                        break

                if not profile_found:
                    st.error('Profile not found. Please check your email.')
                else:
                    st.rerun()