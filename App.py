
import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO
#from API import transfer_style


#这里改标题，page title后面的引号内容是标题，icon里面是网页标志
st.set_page_config(page_title="The Romance of West Chamber",
                   page_icon="./assets/favicon.png", layout="centered")

# -------------Header Section------------------------------------------------

title = '<p style="text-align: center;font-size: 50px;font-weight: 350;font-family:Cursive "> The Romance of West Chamber </p>'
st.markdown(title, unsafe_allow_html=True)

# CSS来改变背景色
#https://htmlcolorcodes.com/zh/ 这个网站上找一个想要的背景色把井号的代码复制到下面这一小段的background color后面
def set_bg_color():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #D6C49C;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_bg_color()
# def set_video_size():
#     st.markdown(
#         """
#         <style>
#         .element-container .stVideo video {
#             width: 300;
#             height: 300;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# set_video_size()


#这段写引子，<b><i>xxxxxx</i></b>，xxxx部分是黑体（b）和斜体（i）举一反三
#We 开始后面都是正文
st.markdown(
    "<b> <i> The painting has come to life! </i> </b>  &nbsp; Step into the world depicted by Wang Shuhui and immerse yourself in the story of The Romance of the Western Chamber.", unsafe_allow_html=True
)




#下面这一大段是主要的展示部分，coll是左边的一列，colr是右边的一列，默认展示动图，如果太小自行在外面放大（就是把动图本身放大），别试着在网页里放大，st容器有问题，caption对应的是每一列的文字部分
#默认展示动图，如果要展示视频就取消colr下面两行的注释，并且注释掉最上面一行
coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("1-talk.mp4")
#st.image(image="./assets/nst.png")
with colr:
    st.image("1-gif.gif", caption='Encounter, Room Rental, Commotion')
    # st.video("./materials/video/1-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
st.caption("During the Tang Dynasty, Cui Xiangguo died, and his wife Cui and daughter Yingying took him home and lived in the Pujiu Temple on their way. When Zhang Junrui, a scholar, traveled to Chang'an to take the exams, he passed by the temple and fell in love with Yingying at first sight.")
st.caption("Since meeting Yingying, Zhang Sheng decides to stay at the temple and asks the abbot for a room in the west chamber.")
st.caption("Zhang Sheng met Hongniang, said: “My name is Zhang Gong, twenty-three years old, has not married. May I know if your master is married?” Hongniang turned around and left.")


coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("2-talk.mp4")
    st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
#st.image(image="./assets/nst.png")
with colr:
    st.image("2-gif.gif", caption='我也不知道这是啥但是好像传gif就是这么简单')
    # st.video("./materials/video/2-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("3-talk.mp4")
    st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
#st.image(image="./assets/nst.png")
with colr:
    st.image("3-gif.gif", caption='我也不知道这是啥但是好像传gif就是这么简单')
    # st.video("./materials/video/3-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("4-talk.mp4")
    st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
#st.image(image="./assets/nst.png")
with colr:
    st.image("4-gif.gif", caption='我也不知道这是啥但是好像传gif就是这么简单')
    # st.video("./materials/video/4-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("5-talk.mp4")
    st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
#st.image(image="./assets/nst.png")
with colr:
    st.image("5-gif.gif", caption='我也不知道这是啥但是好像传gif就是这么简单')
    # st.video("./materials/video/5-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")

st.markdown("</br>", unsafe_allow_html=True)





# -------------Sidebar Section------------------------------------------------
#这一段是左侧边栏展示的内容
#这里开始侧边栏设计
with st.sidebar:
    #这一一坨里面放的东西展示在最上面，呈一列展示
    #替换掉下方引号里的中文内容 切记是中文内容，别乱删别的
    st.image(image="speed-brush.gif")
    st.markdown("</br>", unsafe_allow_html=True)

    st.markdown('<p style="font-size: 25px;font-weight: 550;">The Story 🎨</p>',
                unsafe_allow_html=True)
    st.markdown('The Romance of West Chamber',
                unsafe_allow_html=True)
    st.caption("The story originated from legendary novel The Legend of Yingying in the Tang Dynasty, which recounts the love between Zhang Gong, a scholar, and Cui Yingying, the daughter of Cui Xiangguo, who was also living in the Puyao Temple. With the help of a servant girl, the two got together. Later, Zhang Gong took the examination and became a high-ranking official, but abandoned Yingying, resulting in a love tragedy. This story was adapted into a play by many literati. The Romance of the West Chamber, written by Wang Shifu, was created on these foundations.")

    st.markdown('<p style="font-size: 25px;font-weight: 550;">The Painter 🎨</p>',
                unsafe_allow_html=True)
    st.markdown('Wang Shuhui',
                unsafe_allow_html=True)
    st.caption("Wang Shuhui (1912-1985), courtesy name Yufen, born in Tianjin, was a famous modern female painter of heavy color figures. She is good at inheriting the excellent tradition of line drawing in Chinese painting and absorbing the perspective and anatomical method of Western painting.")
    col1, col2 = st.columns(2)
    with col1:
        st.image(image="wsh3.jpg")
    with col2:
        st.image(image="wsh2.jpg")








