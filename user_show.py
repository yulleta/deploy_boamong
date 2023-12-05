import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Firebase 초기화 체크 및 실행
if not firebase_admin._apps:
    firebase_config = {
        "type": st.secrets["firebase"]["type"],
        "project_id": st.secrets["firebase"]["project_id"],
        "private_key_id": st.secrets["firebase"]["private_key_id"],
        "private_key": st.secrets["firebase"]["private_key"],
        "client_email": st.secrets["firebase"]["client_email"],
        "client_id": st.secrets["firebase"]["client_id"],
        "auth_uri": st.secrets["firebase"]["auth_uri"],
        "token_uri": st.secrets["firebase"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
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


def show_user_page():
    profiles = db.collection('profile').where('email', '==', st.session_state['email']).stream()

    for profile in profiles:
        profile_data = profile.to_dict()
        if profile_data.get('email') == st.session_state['email']:
            if st.button('프로필 수정하기'):
                st.session_state['profile_modify'] = 'modify'
                st.rerun()
            
            st.markdown("#### 🧙 내 프로필 \n")
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
                st.markdown("##### 🔹 소개 링크 / 연락처")
                st.markdown(f'**{profile_data.get("link")}**')
            
            st.markdown("#### 🔮 시각화 / 분석 / 엔지니어링 LEVEL")
            conf_data = [profile_data.get("visual_conf") / 10, profile_data.get("analy_conf") / 10, profile_data.get("engin_conf") / 10, profile_data.get("program_conf") / 10]
            fig = None
            placeholder = st.empty()
            
            placeholder.info("정보를 불러오는 중...")
            if not fig:
                fig = plot_circle(conf_data)
                st.pyplot(fig)
                placeholder.empty()
            
            
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
            
            st.markdown("#### 🎨 생성한 아이디어")
            ideas = db.collection('idea').where('who', '==', st.session_state['email']).stream()
            
            for idea in ideas:
                idea_data = idea.to_dict()
                if idea_data.get('who') == st.session_state['email']:
                    if st.session_state['idea_modify'] == 'read' or idea.id != st.session_state['idea_modify']:
                        # Firestore에서 해당 아이디어 문서를 가져옵니다.
                        idea_document_ref = db.collection('idea').document(idea.id)
                        idea_document = idea_document_ref.get()
                        current_status = idea_document.to_dict().get('status')
                        if current_status:
                            status = ' (모집 중)'
                        else:
                            status = ' (모집 완료)'
                        
                        with st.expander(idea_data.get('emoji') + idea_data.get('headliner') + status):
                            
                            st.subheader("아이디어 한줄소개")
                            headliner = idea_data.get('headliner')
                            st.markdown(f'**{headliner}**')
                            
                            st.subheader("이모지")
                            emoji = idea_data.get('emoji')
                            st.markdown(f'**{emoji}**')
                            
                            st.subheader("What?")
                            what = idea_data.get('what')
                            st.markdown(f'**{what}**')
                            
                            st.subheader("Why?")
                            why= idea_data.get('why')
                            st.markdown(f'**{why}**')
                            
                            st.subheader("How?")
                            how = idea_data.get('how')
                            st.markdown(f'**{how}**')
                            
                            st.subheader("When?")
                            when = idea_data.get('when')
                            st.markdown(f'**{when}**')

                            st.subheader("참고 링크")
                            link = idea_data.get('link')
                            st.markdown(f'**{link}**')
                            
                            if st.button("수정하기", key = idea.id +"수정"):
                                st.session_state['idea_modify'] = idea.id
                                st.rerun()

                            st.caption("모집 완료 상태가 되면 idea 목록에 해당 idea 정보가 뜨지 않습니다")
                            if idea_document.exists and current_status == True:
                                if st.button("모집 완료하기", key=idea.id + "모집완료"):      
                                    # status 값을 반전시킵니다.
                                    new_status = not current_status

                                    # 문서의 status를 업데이트합니다.
                                    idea_document_ref.update({'status': new_status})
                                    st.rerun()
                                    
                            elif idea_document.exists and current_status == False:
                                if st.button("모집 상태로 바꾸기", key=idea.id + "모집 중"):      
                                    # status 값을 반전시킵니다.
                                    new_status = not current_status

                                    # 문서의 status를 업데이트합니다.
                                    idea_document_ref.update({'status': new_status})
                                    st.rerun()

                            
                            # '삭제하기' 버튼
                            if st.button("삭제하기", key=idea.id + "삭제"):
                                # 세션 상태에 삭제할 문서 ID 저장
                                st.session_state['delete_id'] = idea.id

                                # Firestore에서 문서 삭제
                                document_id = st.session_state['delete_id']  # 세션 상태에서 문서의 ID를 가져옴
                                # Firestore 문서 삭제 로직
                                db.collection('idea').document(document_id).delete()
                                st.write('삭제되었습니다.')

                                del st.session_state['delete_id']  # 세션 상태에서 삭제 ID 제거
                                st.rerun()
                    else:
                        with st.expander(idea_data.get('emoji') + idea_data.get('headliner'), expanded = True):
                            st.subheader("아이디어 한줄소개")
                            headliner = st.text_input('아이디어 한줄 소개', value = idea_data.get('headliner'))
                            
                            st.subheader("이모지")
                            emoji = st.text_input('아이디어를 나타내는 대표 이모지 하나를 입력해주세요!', value = idea_data.get('emoji'))
                            
                            st.subheader("What?")
                            what = st.text_area('어떤 아이디어인가요?', value = idea_data.get('what'), key = idea.id + 'what')
                            
                            st.subheader("Why?")
                            why = st.text_area('왜 이 아이디어를 실행해보면 좋은가요?',value = idea_data.get('why'))
                            
                            st.subheader("How?")
                            how = st.text_area('대략 어떻게 아이디어를 실행해볼 생각인가요?', value = idea_data.get('how'))
                            
                            st.subheader("When?")
                            when = st.text_area('아이디어를 실행하는 기간 / 실행을 시작하는 기간은 언제로 예상하나요? 꼭 지금 당장 실행하지 않아도 됩니다', value = idea_data.get('when'))

                            st.subheader("참고 링크")
                            link = st.text_input('아이디어를 더 자세히 소개할 수 있는 참고 링크를 첨부해 주세요', value = idea_data.get('link'))
                            
                            st.subheader("예상 구현 난이도")
                            difficulty = st.slider('난이도', 0, 20, key = idea.id + "create_idea_difficulty", value = idea_data.get('difficulty'))
                            st.subheader("아이디아의 파급력 / 임팩트 정도")
                            impact = st.slider('임팩트', 0, 20, key = idea.id + "create_idea_impact", value = idea_data.get('impact'))
                            
                            if st.button("정보 업데이트", key = idea.id +"수정 완료"):
                            
                                updated_idea_data = {
                                    "who" : idea_data.get('who'),
                                    "what" : what,
                                    "why" : why,
                                    "how" : how,
                                    "when" : when,
                                    "link" : link,
                                    "difficulty" : difficulty,
                                    "impact" : impact,
                                    "headliner" : headliner,
                                    "emoji" : emoji,
                                    "status" : idea_data.get('status'),
                                }
                                
                                db.collection('idea').document(idea.id).set(updated_idea_data, merge=True)
                                st.session_state['idea_modify'] = 'read'
                                st.rerun()
                            
            
            st.markdown("#### 🔖 북마크")
            
            profiles = db.collection('profile').where('email', '==', st.session_state['email']).stream()

            for profile in profiles:
                profile_data = profile.to_dict()
                # 'bookmark' 필드가 없는 경우 빈 리스트로 처리
                bookmarks = profile_data.get("bookmark", [])
                for bookmarked in bookmarks:
                    # 실제 문서 데이터를 가져옴
                    idea_document = db.collection('idea').document(bookmarked).get()
                    if idea_document.exists:
                        # 문서 데이터에서 필요한 정보 추출
                        idea_data = idea_document.to_dict()
                        headliner = idea_data.get('headliner')  # 필드 이름 확인 및 수정
                        emoji = idea_data.get('emoji')
                        
                        with st.expander(f"{emoji} {headliner}"):
                            headliner = idea_data.get('headliners')
                            st.markdown(f'**{headliner}**')
                            
                            st.subheader("이모지")
                            emoji = idea_data.get('emoji')
                            st.markdown(f'**{emoji}**')
                            
                            st.subheader("What?")
                            what = idea_data.get('what')
                            st.markdown(f'**{what}**')
                            
                            st.subheader("Why?")
                            why= idea_data.get('why')
                            st.markdown(f'**{why}**')
                            
                            st.subheader("How?")
                            how = idea_data.get('how')
                            st.markdown(f'**{how}**')
                            
                            st.subheader("When?")
                            when = idea_data.get('when')
                            st.markdown(f'**{when}**')

                            st.subheader("참고 링크")
                            link = idea_data.get('link')
                            st.markdown(f'**{link}**')

                            if st.button("북마크 해제하기", key = idea_document.id):
                                profiles = db.collection('profile').where('email', '==', st.session_state['email']).stream()

                                for profile in profiles:
                                    profile_data = profile.to_dict()
                                    if profile_data.get('email') == st.session_state['email']:
                                        # 북마크 리스트 초기화 및 업데이트
                                        bookmarks = profile_data.get('bookmark', [])
                                        bookmarks.remove(idea_document.id)
                                        updated_data = {"bookmark": bookmarks}

                                        # 해당 문서 업데이트
                                        db.collection('profile').document(profile.id).set(updated_data, merge=True)
                                        st.rerun()
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")

            with st.expander("회원 탈퇴하기"):
                st.warning("❗ (아쉬워요 ㅠ) 회원 탈퇴하면 모든 정보가 삭제됩니다.")
                if st.button("회원 탈퇴하기"):
                    # 사용자 이메일로 프로필 문서 검색 및 삭제
                    profiles = db.collection('profile').where('email', '==', st.session_state['email']).stream()
                    for profile in profiles:
                        db.collection('profile').document(profile.id).delete()

                    # 사용자 이메일로 생성한 아이디어 문서 검색 및 삭제
                    ideas = db.collection('idea').where('who', '==', st.session_state['email']).stream()
                    for idea in ideas:
                        db.collection('idea').document(idea.id).delete()

                    st.session_state['logged_in'] = False
                    st.session_state['current_page'] = 'signin'
                    st.session_state['signed_up'] = False
                    st.rerun()
