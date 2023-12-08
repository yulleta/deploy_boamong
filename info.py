import streamlit as st

def show_info_page():
    st.markdown("<center><h1>🎨🔨✨🎈💡🐘</h1></center>", unsafe_allow_html=True)
    st.markdown("<center><h3>보아몽 공작소에 오신 것을 환영합니다!</h3></center>", unsafe_allow_html=True)
    
    video_file = open('보아몽 공작소 소개 영상.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    
    st.markdown("<h4><br/><br/><br/>🎈누구를 위한 소모임인가요?</h4>", unsafe_allow_html=True)
    st.markdown("<h5>우리는 왜 빅데이터를 공부할까요?</h5>", unsafe_allow_html=True)
    st.markdown("<h6>데이터는 사회와 사람들의 영감, 생각을 반영하는 거울입니다.</h6><br/>\
                데이터를 통해 현실을 분석하고 미래를 예측하며 어떤 어려운 문제들도 해결할 수 있습니다.<br/> \
                그리고 이러한 과정은 무작위적이고 보잘것 없어 보이는 아이디어에서부터 시작할 수 있습니다.<br/>\
                <br/>\
                하지만 너무 조급해하지는 않아도 됩니다. <br/>\
                <strong>문득문득 생각나는 아이디어들을 자유롭게 나누며 영감을 공유하고, </br> \
                실행해보면 재밌을거 같은 아이디어를 <br/>\
                팀원들과 함께 실현해보고 싶은 보아즈 부원들을 위한 모임입니다.</strong>\
                ", unsafe_allow_html=True)
    
    
    st.markdown("<h4><br/>🎈어떤 활동을 하나요?</h4>", unsafe_allow_html=True)
    st.markdown("<ul>\
                    <li><h6>1~2달에 한 번씩 모여 프로젝트 아이디어를 공유합니다</h6>\
                        어떤 것에 영감을 받아 이 아이디어를 생각하게 되었는지,<br/>\
                        이 아이디어를 어떻게 실행하면 좋을 지 <br/>\
                        대략적으로라도 구체화하여 보아즈 부원들과 공유합니다.</li>\
                    </br>\
                    <li><h6>각종 빅데이터 관련 행사 참여하고 매일 빅데이터 관련 뉴스를 접합니다</h6>\
                        최신 트렌드를 아는 것이 중요한 IT업게,</br> \
                        빅데이터에 관심이 많은 보아즈 부원들과 함께 각종 빅데이터 관련 컨퍼런스/행사에 참여해보세요.</br>\
                        매일 슬랙 알림을 통해 최신 IT 핫토픽 뉴스들도 접해보세요.</li>\
                    </br>\
                    <li><h6>웹페이지를 통해 재밌어 보이는 아이디어를 선정하고<br/>\
                        아이디어를 함께 실행할 팀원을 구합니다</h6>\
                        웹페이지를 통해 아이디어의 임팩트(파장력), 구현 난이도 등을 고려하여 아이디어를 선정하고 </br>\
                        필요한 기술 스택, 기술 수준에 적합한 동아리 부원을 구해보세요. <br/>\
                        유사도 분석을 통해 필요한 팀원을 쉽게 구할 수 있습니다. \
                        </li>\
                    <br/>\
                    <li><h6>관심분야 및 희망 하는 진로가 비슷한 사람들을 구해보세요</h6>\
                        동아리에 나와 관심 분야가 일치하는 사람은 누가 있는지,<br/> \
                        같이 진로와 관련된 이야기를 할 수 있는 부원은 누가 있는지 자유롭게 탐색해 보세요. <br/>\
                    </li>\
            </ul>", unsafe_allow_html=True)
    
    st.markdown("<h4><br/>🤔꼭 성과를 내야 하는 활동인가요?</h4>", unsafe_allow_html=True)
    st.markdown("마감 기한이 정해진 과제처럼 부담을 가지지 않으셔도 됩니다. <br/>\
                마음이 맞는 사람들과 함께 자발적, 자율적으로 프로젝트를 진행하셔도 됩니다. <br/>\
                자유롭게 소모임에 참여하고 사이트를 이용하며 <br/>\
                재밌는 아이디어 공유의 장이 되었으면 하는 마음입니다 <br/>\
                보아즈 부원들의 톡톡 튀는 아이디어와 즐기며 참여할 수 있는 열정을 기대합니다 :)", unsafe_allow_html=True)