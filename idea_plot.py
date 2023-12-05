import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from streamlit_plotly_events import plotly_events
from PIL import Image
import matplotlib.pyplot as plt


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

def show_idea_plot():
    
    st.header("📢 팀원 모집 중인 아이디어")
    
    ideas = db.collection('idea').stream()
    profiles = db.collection('profile')
    
    # Initialize lists to store the data
    impact_values = []
    difficulty_values = []
    emojis = []
    headliners = []
    how = []
    what = []
    when = []
    who = []
    why = []
    link = []
    status = []
    id = []
    
    # Iterate through documents and extract data
    for idea in ideas:
        data = idea.to_dict()
        
        who_email = data.get('who')
        profile_docs = profiles.where('email', '==', who_email).stream()
        
        impact_values.append(data.get('impact', 0))  # Replace 0 with a default value if needed
        difficulty_values.append(data.get('difficulty', 0))  # Replace 0 with a default value if needed
        emojis.append(data.get('emoji', "🎈")) # Add your label logic here
        headliners.append(data.get('headliner'))
        how.append(data.get('how'))
        what.append(data.get('what'))
        when.append(data.get('when'))
        why.append(data.get('why'))
        link.append(data.get('link'))
        status.append(data.get('status'))
        id.append(idea.id)      
        for profile in profile_docs:
            profile_data = profile.to_dict()
            who.append(str(profile_data.get('year', 'Unknown')) +'기 '+ profile_data.get('name', 'Unknown'))  # 이름이 없는 경우 기본값 'Unknown'
          
            
    # Normalize the values from 0-20 to 0-1
    impact_normalized = [x / 20 for x in impact_values]
    difficulty_normalized = [x / 20 for x in difficulty_values]
    
    df = pd.DataFrame({
        '임팩트': impact_normalized,
        '구현 난이도': difficulty_normalized,
        'label': emojis,
        'headliners' : headliners,
        'how' : how,
        'what' : what,
        'when' : when,
        'why' : why,
        'link' : link,
        'status' :status,
        'who' : who,
        "id" : id
    })
    
    # Remove rows where 'status' is False
    df = df[df['status']]

    # Adjust '임팩트' values to avoid overlap
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            if df.iloc[i]['임팩트'] == df.iloc[j]['임팩트'] and df.iloc[i]['구현 난이도'] == df.iloc[j]['구현 난이도']:
                # Increment one of the '임팩트' values to avoid overlap
                df.at[j, '임팩트'] -= 0.02
        
    # Create a scatter plot
    fig = px.scatter(df, x='임팩트', y='구현 난이도', text='label')
    fig.update_traces(textfont=dict(size=25))

    # Capture click events on the scatter plot
    selected_points = plotly_events(fig)


    # Display the details of the selected point
    if selected_points:
        selected_index = selected_points[0]['pointIndex']
        selected_df = df.iloc[selected_index]
        
        st.subheader("아이디어 제공한 사람")
        who = selected_df['who']
        
        placeholder = st.empty()
        placeholder.info("정보를 불러오는 중...")
        
        with st.expander(f'**{who}**'):
            profiles = db.collection('profile').where('name', '==', who).stream()

            for profile in profiles:
                profile_data = profile.to_dict()

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
            
            placeholder.empty()
            
            
        
        st.subheader("아이디어 한줄 소개")
        headliner = selected_df['headliners']
        st.markdown(f'**{headliner}**')
        
        st.subheader("이모지")
        emoji = selected_df['label']
        st.markdown(f'**{emoji}**')
        
        st.subheader("What?")
        what = selected_df['what']
        st.markdown(f'**{what}**')
        
        st.subheader("Why?")
        why= selected_df['why']
        st.markdown(f'**{why}**')
        
        st.subheader("How?")
        how = selected_df['how']
        st.markdown(f'**{how}**')
        
        st.subheader("When?")
        when = selected_df['when']
        st.markdown(f'**{when}**')

        st.subheader("참고 링크")
        link = selected_df['link']
        st.markdown(f'**{link}**')
        

        if st.button("✨북마크하기"):
            profiles = db.collection('profile').where('email', '==', st.session_state['email']).stream()

            for profile in profiles:
                profile_data = profile.to_dict()
                if profile_data.get('email') == st.session_state['email']:
                    # 북마크 리스트 초기화 및 업데이트
                    bookmarks = profile_data.get('bookmark', [])
                    if selected_df['id'] not in bookmarks:
                        bookmarks.append(selected_df['id'])
                        updated_data = {"bookmark": bookmarks}

                        # 해당 문서 업데이트
                        db.collection('profile').document(profile.id).set(updated_data, merge=True)
                        st.success("북마크 완료!")
                        break
                    else:
                        st.info("이미 북마크한 아이디어입니다!")


                    
    else:
        st.subheader("이모지를 선택하면 해당 아이디어 정보를 볼 수 있어요!")