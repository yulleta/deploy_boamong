import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

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

googledatastudio  = Image.open("./img/visual/googledatastudio.png")
powerbi = Image.open("./img/visual/powerbi.png")
tableau  = Image.open("./img/visual/tableau.png")

visual_img = {
    'googleDataStudio' : googledatastudio,
    'powerBI' : powerbi, 
    'Tableau' : tableau,
}

time= Image.open("./img/analy/time.png")
cv = Image.open("./img/analy/cv.png")
nlp = Image.open("./img/analy/nlp.png")
pytorch = Image.open("./img/analy/pytorch.png")
r = Image.open("./img/analy/r.png")
rl= Image.open("./img/analy/rl.png")
rs = Image.open("./img/analy/rs.png")
tensorflow = Image.open("./img/analy/tensorflow.png")
multi = Image.open("./img/analy/multi.png")


analy_img = {
    "시계열" : time,
    "컴퓨터 비전(CV)" : cv,
    "멀티모달(multi-modal)" : multi,
    "자연어처리(NLP)" : nlp,
    "pytorch": pytorch,
    "R" : r,
    "강화학습(RL)" : rl,
    "추천시스템(RS)" : rs,
    "tensorflow" : tensorflow
}

airflow = Image.open("./img/engin/apache_airflow.png")
flink = Image.open("./img/engin/apache_flink.png")
hadoop = Image.open("./img/engin/apache_hadoop.png")
kafka = Image.open("./img/engin/apache_kafka.png")
spark = Image.open("./img/engin/apache_spark.png")
storm = Image.open("./img/engin/apache_storm.png")
aws = Image.open("./img/engin/aws.png")
azure = Image.open("./img/engin/azure.png")
docker = Image.open("./img/engin/docker.png")
gcp = Image.open("./img/engin/gcp.png")
googlebigquery = Image.open("./img/engin/googlebigquery.png")
kubernets = Image.open("./img/engin/kubernets.png")
mongodb= Image.open("./img/engin/mongodb.png")
mysql = Image.open("./img/engin/mysql.png")
post = Image.open("./img/engin/post.png")
snowflake = Image.open("./img/engin/snowflake.png")

engin_img = {'apache airflow' : airflow, 
            'apache flink' : flink, 
            'apche hadoop' : hadoop,
            'apache kafka' : kafka,
            'apache spark' : spark,
            'apache storm' : storm,
            'aws' : aws,
            'azure' : azure,
            'docker' : docker,
            'gcp' : gcp,
            'googlebigquery' : googlebigquery, 
            'kubernets' : kubernets,
            'mongodb' : mongodb,
            'mysql' : mysql,
            'postgresql' : post,
            'snowflake' : snowflake}

android = Image.open("./img/program/android.png")
django = Image.open("./img/program/django.png")
flask = Image.open("./img/program/flask.png")
nodejs = Image.open("./img/program/nodejs.png")
react = Image.open("./img/program/react.png")
reactnative = Image.open("./img/program/reactnative.png")
spring = Image.open("./img/program/spring.png")
streamlit = Image.open("./img/program/streamlit.png")
swift = Image.open("./img/program/swift.png")
unity = Image.open("./img/program/unity.png")
unreal = Image.open("./img/program/unreal.png")
vue = Image.open("./img/program/vue.png")

program_img = {'React.js' : react,
            'Vue.js' : vue, 
            'streamlit' : streamlit, 
            'swift' : swift, 
            'android' : android, 
            'react native' : reactnative, 
            'spring' : spring, 
            'node.js' : nodejs, 
            'flask' : flask, 
            'django' : django, 
            'unity' : unity, 
            'unreal' : unreal}


def plot_circle(data):
    # 원 위의 3개 지점에 대한 각도
    angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False)

    # 극좌표계 그래프 초기화
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    # 데이터 포인트를 원의 둘레에 플롯
    ax.scatter(angles, data, color='#c5a6ff', s=100)  # 원 위의 점들

    # 세 점을 연결하는 선 그리기
    for i in range(len(angles)):
        next_index = (i + 1) % len(angles)
        ax.plot([angles[i], angles[next_index]], [data[i], data[next_index]], color='#c5a6ff', linewidth = 4)  # 삼각형의 선
        ax.fill(angles, data, color='#c5a6ff', alpha=0.25)
        
    # 120도 간격의 방향 설정
    ax.set_xticks(np.pi/180. * np.linspace(0,  360, 4, endpoint=False))

    # 라벨 추가
    ax.set_xticklabels(['visualization', 'analysis', 'engineering', 'programming'], fontsize=20, color='#813dff')

    # 원의 경계 그리기
    ax.plot(angles, [1]*len(angles), color='white', alpha = 0)

    return fig

def show_ppl_plot():
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔨 STACK", "🔮 LEVEL", "😆 관심분야", "✨희망진로", "🔎사람검색"])

    with tab1:
        profiles = db.collection('profile').stream()
        
        st.subheader("필요한 기술 STACK을 가진 사람을 찾아보세요!")
        st.markdown("**필요한 기술스택들과 가장 일치하는 사람들을 최대 15명까지 보여줍니다**")
        st.markdown("❗ 기술스택이 크게 상관 없는 항목은 비워주세요!")
        
        visual_stack_options = ['없음', 'googleDataStudio', 'powerBI', 'Tableau']
        analy_stack_options = ['없음', '시계열', '컴퓨터 비전(CV)', '멀티모달(multi-modal)', '자연어처리(NLP)', '강화학습(RL)', '추천시스템(RS)', 'pytorch', 'R', 'tensorflow']
        engin_stack_options = ['없음', 'apache airflow', 'apache flink', 'apche hadoop', 'apache kafka', 'apache spark', 'apache storm',\
            'aws', 'azure', 'docker', 'gcp', 'googlebigquery', 'kubernets', 'mongodb', 'mysql', 'postgresql', 'snowflake']
        program_stack_options = ['없음', 'React.js', 'Vue.js', 'streamlit', 'swift', 'android', 'react native', 'spring', 'node.js', 'flask', 'django', 'unity', 'unreal']

        # Stacks
        user_visual_stacks = st.multiselect('Visual Stacks', options=visual_stack_options, key = "user_modify_visual_stacks")
        user_analy_stacks = st.multiselect('Analytical Stacks', options=analy_stack_options, key = "user_modify_analy_stacks")
        user_engin_stacks = st.multiselect('Engineering Stacks', options=engin_stack_options, key = "user_modify_engin_stacks")
        user_program_stacks = st.multiselect('Programming Stacks', options=program_stack_options, key = "user_modify_program_stacks")
        
        # 각 프로필의 일치도를 계산
        def stack_calculate_match(profile):
            match_count = 0
            match_count += len(set(profile['visual_stacks']) & set(user_visual_stacks))
            match_count += len(set(profile['analy_stacks']) & set(user_analy_stacks))
            match_count += len(set(profile['engin_stacks']) & set(user_engin_stacks))
            match_count += len(set(profile['program_stacks']) & set(user_program_stacks))
            return match_count
        
        def calculate_match_items(profile):
            matching_visual_stacks = list(set(profile['visual_stacks']) & set(user_visual_stacks))
            matching_analy_stacks = list(set(profile['analy_stacks']) & set(user_analy_stacks))
            matching_engin_stacks = list(set(profile['engin_stacks']) & set(user_engin_stacks))
            matching_program_stacks = list(set(profile['program_stacks']) & set(user_program_stacks))

            return matching_visual_stacks, matching_analy_stacks, matching_engin_stacks, matching_program_stacks
        
        if len(st.session_state['profiles_search_stack']) != 0:
            st.session_state['profiles_search_stack'] = []
        
        for profile in profiles:
            profile_data = profile.to_dict()
            profile_dict = {}
            profile_dict ['name'] = profile_data.get('name')
            profile_dict ['year'] = profile_data.get('year')
            profile_dict['visual_stacks'] = profile_data.get('visual_stacks')
            profile_dict['analy_stacks'] = profile_data.get('analy_stacks')
            profile_dict['engin_stacks'] = profile_data.get('engin_stacks')
            profile_dict['program_stacks'] = profile_data.get('program_stacks')
            matching_visual_stacks, matching_analy_stacks, matching_engin_stacks, matching_program_stacks = calculate_match_items(profile_data)
            profile_dict['matching_visual_stacks'] = matching_visual_stacks
            profile_dict['matching_analy_stacks'] = matching_analy_stacks
            profile_dict['matching_engin_stacks'] = matching_engin_stacks
            profile_dict['matching_program_stacks'] = matching_program_stacks
            profile_dict['visual_conf'] = profile_data.get('visual_conf')
            profile_dict['analy_conf'] = profile_data.get('analy_conf')
            profile_dict['engin_conf'] = profile_data.get('engin_conf')
            profile_dict['program_conf'] = profile_data.get('program_conf')
            st.session_state['profiles_search_stack'].append(profile_dict)
        
        # 일치도에 따라 프로필 정렬 및 결과 출력
        if st.button("찾기", key="stack_search"):
            
            sorted_profiles = sorted(st.session_state['profiles_search_stack'], key=stack_calculate_match, reverse=True) 
            
            if len(sorted_profiles) > 15:
                sorted_profiles = sorted_profiles[:15]
            
            # 결과 출력
            for profile in sorted_profiles:             
                with st.expander(str(profile['year']) + "기 " + profile['name']):
                    st.markdown("**일치하는 스택**")
                    if len(profile['matching_visual_stacks']) != 0:
                        st.markdown(profile['matching_visual_stacks'])
                    
                    if len(profile['matching_analy_stacks']) != 0:
                        st.markdown(profile['matching_analy_stacks'])
                    
                    if len(profile['matching_engin_stacks']) != 0:
                        st.markdown(profile['matching_engin_stacks'])
                    
                    if len(profile['matching_program_stacks']) != 0:
                        st.markdown(profile['matching_program_stacks'])

                    if (len(profile['matching_visual_stacks']) == 0) and (len(profile['matching_analy_stacks']) == 0) and\
                        (len(profile['matching_engin_stacks']) == 0) and (len(profile['matching_program_stacks']) == 0):
                            st.markdown("일치하는 스택 없음")
                        
                    st.markdown("**시각화 STACKS :** " + str(profile['visual_stacks']))
                    st.markdown("**분석 STACKS :** "+ str(profile['analy_stacks']))
                    st.markdown("**엔지니어링 STACKS :** "+ str(profile['engin_stacks']))
                    st.markdown("**프로그래밍 STACKS :** "+ str(profile['program_stacks']))
                
                    fig = plot_circle([profile['visual_conf'] / 10, profile['analy_conf'] / 10, profile['engin_conf'] / 10, profile['program_conf'] / 10])
                    st.pyplot(fig)
    with tab2:
        profiles = db.collection('profile').stream()
        
        st.subheader("필요한 LEVEL을 가진 사람을 찾아보세요!")
        st.markdown("**기술스택별 필요한 LEVEL을 가진 가장 일치하는 사람들을 최대 15명까지 보여줍니다**")
        st.markdown("❗ 기술스택의 LEVEL이 크게 상관 없는 항목은 비워주세요!")
    
        
        # Confidence levels
        user_visual_conf = st.slider('Visual Confidence', 0, 10, key = "user_modify_visual_conf", value = 0)
        user_analy_conf = st.slider('Analytical Confidence', 0, 10, key = "user_modify_analy_conf", value = 0)
        user_engin_conf = st.slider('Engineering Confidence', 0, 10, key = "user_engin_conf", value = 0)
        user_program_conf = st.slider('Programming Confidence', 0, 10, key = "user_program_conf", value = 0)
        
        user_conf = [user_visual_conf/10, user_analy_conf/10, user_engin_conf/10, user_program_conf/10]
        
        def cosine_similarity(vec1, vec2):
            dot_product = np.dot(vec1, vec2)
            norm_vec1 = np.linalg.norm(vec1)
            norm_vec2 = np.linalg.norm(vec2)
            return dot_product / (norm_vec1 * norm_vec2)

        def level_calculate_match(profile):
            profile_conf = [profile['visual_conf'], profile['analy_conf'], profile['engin_conf'], profile['program_conf']]
            
            # 코사인 유사도 계산
            similarity = cosine_similarity(profile_conf, user_conf)
            return similarity
        
        if len(st.session_state['profiles_search_conf']) != 0:
                st.session_state['profiles_search_conf'] = []
            
        for profile in profiles:
            profile_data = profile.to_dict()
            profile_dict = {}
            profile_dict ['name'] = profile_data.get('name')
            profile_dict ['year'] = profile_data.get('year')
            profile_dict['visual_stacks'] = profile_data.get('visual_stacks')
            profile_dict['analy_stacks'] = profile_data.get('analy_stacks')
            profile_dict['engin_stacks'] = profile_data.get('engin_stacks')
            profile_dict['program_stacks'] = profile_data.get('program_stacks')
            profile_dict['visual_conf'] = profile_data.get('visual_conf')
            profile_dict['analy_conf'] = profile_data.get('analy_conf')
            profile_dict['engin_conf'] = profile_data.get('engin_conf')
            profile_dict['program_conf'] = profile_data.get('program_conf')
            st.session_state['profiles_search_conf'].append(profile_dict)
        
        if st.button("찾기", key="conf_search"):
            
            sorted_profiles = sorted(st.session_state['profiles_search_conf'], key=level_calculate_match, reverse=True) 
            
            if len(sorted_profiles) > 15:
                sorted_profiles = sorted_profiles[:15]
            
            # 결과 출력
            for profile in sorted_profiles:                
                with st.expander(str(profile['year']) + "기 " + profile['name']):
                    st.markdown("**시각화 STACKS :** " + str(profile['visual_stacks']))
                    st.markdown("**분석 STACKS :** "+ str(profile['analy_stacks']))
                    st.markdown("**엔지니어링 STACKS :** "+ str(profile['engin_stacks']))
                    st.markdown("**프로그래밍 STACKS :** "+ str(profile['program_stacks']))
                
                    fig = plot_circle([profile['visual_conf'] / 10, profile['analy_conf'] / 10, profile['engin_conf'] / 10, profile['program_conf'] / 10])
                    st.pyplot(fig)
        

    with tab3:
        profiles = db.collection('profile').stream()
        
        st.subheader("나와 관심분야가 일치하는 사람을 찾아보세요!")
        interest_options = ["없음", "스포츠⚽", "예술(문화활동)🎨" , "과학기술🧪🔨", "여행🧳", "맛집🍽", "건강💪", "경제💸", "사회🌐"]
        
        user_interest = st.multiselect('관심분야', options=interest_options, key = "user_modify_interest", default="없음")  # interest_options는 관심사 목록

        # 각 프로필의 일치도를 계산
        def interest_calculate_match(profile):
            match_count = 0
            match_count += len(set(profile['interest']) & set(user_interest))
            return match_count
        
        def calculate_match_interests(profile):
            matching_interests = list(set(profile['interest']) & set(user_interest))
            return matching_interests
        
        if len(st.session_state['profiles_search_interest']) != 0:
            st.session_state['profiles_search_interest'] = []
            
        for profile in profiles:
            profile_data = profile.to_dict()
            profile_dict = {}
            profile_dict ['name'] = profile_data.get('name')
            profile_dict ['year'] = profile_data.get('year')
            profile_dict['interest'] = profile_data.get('interest')
            matching_interests = calculate_match_interests(profile_data)
            profile_dict['matching_interests'] = matching_interests
            
            st.session_state['profiles_search_interest'].append(profile_dict)

        # 일치도에 따라 프로필 정렬 및 결과 출력
        if st.button("찾기", key="interest_search"):
            
            sorted_profiles = sorted(st.session_state['profiles_search_interest'], key=interest_calculate_match, reverse=True) 
            
            if len(sorted_profiles) > 15:
                sorted_profiles = sorted_profiles[:15]
            
            def interest_calculate_match(profile):
                match_count = 0
                match_count += len(set(profile['interest']) & set(user_interest))
                return match_count
            
            sorted_profiles = sorted(st.session_state['profiles_search_interest'], key=interest_calculate_match, reverse=True) 
            
            if len(sorted_profiles) > 15:
                sorted_profiles = sorted_profiles[:15]
            
            non_found = True        
            for profile in sorted_profiles:  
                if len(profile['matching_interests']) != 0:  
                    non_found = False         
                    with st.expander(str(profile['year']) + "기 " + profile['name']):
                        st.markdown("**일치하는 희망 진로분야**")
                        st.markdown(profile['matching_interests'])
                        st.markdown("**희망 진로**")
                        st.markdown(profile['interest'])
            if non_found:
                st.markdown("관심 분야가 일치하는 사람이 없습니다")
    with tab4:        
        profiles = db.collection('profile').stream()
        
        st.subheader("나와 희망하는 진로가 일치하는 사람을 찾아보세요!")
        career_options = ['없음', '데이터 분석/시각화', '데이터 과학/ML/DL', '데이터 엔지니어링','프론트엔드', '백엔드','앱개발', '마케팅', '보안']
        
        user_career = st.multiselect('희망진로', options=career_options, key = "user_modify_career", default="없음")  # career_options는 관심사 목록

        # 각 프로필의 일치도를 계산
        def career_calculate_match(profile):
            match_count = 0
            match_count += len(set(profile['career']) & set(user_career))
            return match_count
        
        def calculate_match_careers(profile):
            matching_careers = list(set(profile['career']) & set(user_career))
            return matching_careers
        
        if len(st.session_state['profiles_search_career']) != 0:
            st.session_state['profiles_search_career'] = []
            
        for profile in profiles:
            profile_data = profile.to_dict()
            profile_dict = {}
            profile_dict ['name'] = profile_data.get('name')
            profile_dict ['year'] = profile_data.get('year')
            profile_dict['career'] = profile_data.get('career')
            matching_careers = calculate_match_careers(profile_data)
            profile_dict['matching_careers'] = matching_careers
            
            st.session_state['profiles_search_career'].append(profile_dict)

        # 일치도에 따라 프로필 정렬 및 결과 출력
        if st.button("찾기", key="career_search"):
            
            sorted_profiles = sorted(st.session_state['profiles_search_career'], key=career_calculate_match, reverse=True) 
            
            if len(sorted_profiles) > 15:
                sorted_profiles = sorted_profiles[:15]
            
            def career_calculate_match(profile):
                match_count = 0
                match_count += len(set(profile['career']) & set(user_career))
                return match_count
            
            sorted_profiles = sorted(st.session_state['profiles_search_career'], key=career_calculate_match, reverse=True) 
            
            # 결과 출력
            non_found = True
            for profile in sorted_profiles:
                if len(profile['matching_careers']) != 0:  
                    non_found = False         
                    with st.expander(str(profile['year']) + "기 " + profile['name']):
                        st.markdown("**일치하는 희망 진로분야**")
                        st.markdown(profile['matching_careers'])
                        st.markdown("**희망 진로**")
                        st.markdown(profile['career'])
            if non_found:
                st.markdown("희망 진로가 일치하는 사람이 없습니다")
    with tab5:        
        st.subheader("사람을 검색하고 상세 정보를 알 수 있어요!")
        
        search = st.text_input("이름을 입력하세요")
        
        st.caption("버튼을 클릭해서 검색해주세요. 결과가 뜨지 않으면 다시 버튼을 눌러주세요.")
        if st.button("찾기", key="ppl_search"):
            
            # Firestore 쿼리 실행
            profiles = db.collection('profile').where('name', '==', search).stream()

            # 검색 결과 표시
            found = False

            for profile in profiles:
                profile_data = profile.to_dict()
                found = True  # 일치하는 프로필을 찾았음

                with st.expander(str(profile_data.get("year")) + "기 " + profile_data.get("name")):
                
                    st.markdown("#### 🧙프로필 \n")
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.markdown("##### 🔹 이름")
                        st.markdown(f'**{profile_data.get("name")}**')
                        st.markdown("##### 🔹 관심분야")
                        interests = profile_data.get("interest")
                        for interest in interests:
                            st.markdown(f'**{interest}**')
                    with col2:
                        st.markdown("##### 🔹 기수")
                        st.markdown(f'**{profile_data.get("year")}**')
                        st.markdown("##### 🔹 한줄 소개")
                        st.markdown(f'**{profile_data.get("introduction")}**')

                    with col3:
                        st.markdown("##### 🔹 희망 진로")
                        careers = profile_data.get("career")
                        for career in careers:
                            st.markdown(f'**{career}**')
                        st.markdown("##### 🔹 소개 링크")
                        st.markdown(f'**{profile_data.get("link")}**')
                    
                    st.markdown("#### 🔮 시각화 / 분석 / 엔지니어링 LEVEL")
                    conf_data = [profile_data.get("visual_conf") / 10, profile_data.get("analy_conf") / 10, profile_data.get("engin_conf") / 10, profile_data.get("program_conf") / 10]
                    fig = plot_circle(conf_data)
                    st.pyplot(fig)
                    
                    st.markdown("#### 🔨 시각화 stacks")
                    v_col1, v_col2, v_col3, v_col4, v_col5, v_col6 = st.columns(6)
                    a_cols = [v_col1, v_col2, v_col3, v_col4, v_col5, v_col6]
                    v_num = 0
                    if profile_data.get("visual_stacks") == ['없음']:
                        st.markdown("**없음**")
                    else:
                        for stack in profile_data.get("visual_stacks"):  
                            with a_cols[v_num%6]:
                                st.image(visual_img[stack])
                                st.markdown(f"<center>{profile_data.get('visual_stacks')[v_num]}</center>", unsafe_allow_html=True)
                            v_num+=1
                    
                    st.markdown("#### 🔨 분석 stacks")
                    a_col1, a_col2, a_col3, a_col4, a_col5, a_col6 = st.columns(6)
                    a_cols = [a_col1, a_col2, a_col3, a_col4, a_col5, a_col6]
                    a_num = 0
                    if profile_data.get("analy_stacks") == ['없음']:
                        st.markdown("**없음**")
                    else:
                        for stack in profile_data.get("analy_stacks"):  
                            with a_cols[a_num%6]:
                                st.image(analy_img[stack])
                                st.markdown(f"<center>{profile_data.get('analy_stacks')[a_num]}</center>", unsafe_allow_html=True)
                            a_num+=1
                        
                    st.markdown("#### 🔨 엔지니어링 stacks")
                    e_col1, e_col2, e_col3, e_col4, e_col5, e_col6  = st.columns(6)
                    e_cols = [e_col1, e_col2, e_col3, e_col4, e_col5, e_col6 ]
                    e_num = 0
                    if profile_data.get("engin_stacks") == ['없음']:
                        st.markdown("**없음**")
                    else:
                        for stack in profile_data.get("engin_stacks"):  
                            with e_cols[e_num%6]:
                                st.image(engin_img[stack])
                                st.markdown(f"<center>{profile_data.get('engin_stacks')[e_num]}</center>", unsafe_allow_html=True)
                            e_num+=1
                        
                    st.markdown("#### 🔨 개발 stacks")
                    p_col1, p_col2, p_col3, p_col4, p_col5, p_col6 = st.columns(6)
                    p_cols = [p_col1, p_col2, p_col3, p_col4, p_col5, p_col6 ]
                    p_num = 0
                    if profile_data.get("program_stacks") == ['없음']:
                        st.markdown("**없음**")
                    else:
                        for stack in profile_data.get("program_stacks"):  
                            with p_cols[p_num%6]:
                                st.image(program_img[stack])
                                st.markdown(f"<center>{profile_data.get('program_stacks')[p_num]}</center>", unsafe_allow_html=True)
                            p_num+=1
                    

            if not found:
                st.write("검색된 사람이 없습니다.")

            