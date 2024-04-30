
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
st.caption("  ")



#下面这一大段是主要的展示部分，coll是左边的一列，colr是右边的一列，默认展示动图，如果太小自行在外面放大（就是把动图本身放大），别试着在网页里放大，st容器有问题，caption对应的是每一列的文字部分
#默认展示动图，如果要展示视频就取消colr下面两行的注释，并且注释掉最上面一行
coll, colr = st.columns(2)
# Example Image
with coll:
     st.image("1-gif.gif", caption='Enchantment, Renting of Quarters, Religious Service')
with colr:
     st.video("1-talk.mp4")
#st.image(image="./assets/nst.png")
st.caption("During the Tang Dynasty, Cui Xiangguo died, and his wife Cui and daughter Yingying took him home and lived in the Pujiu Temple on their way. When Zhang Junrui, a scholar, traveled to Chang'an to take the exams, he passed by the temple and fell in love with Yingying at first sight.")
st.caption("Since meeting Yingying, Zhang Sheng decides to stay at the temple and asks the abbot for a room in the west chamber.")
st.caption("Zhang Sheng met Hongniang, said: “My name is Zhang Gong, twenty-three years old, has not married. May I know if your master is married?” Hongniang turned around and left.")
st.caption("  ")
st.caption("  ")

coll, colr = st.columns(2)
# Example Image
with coll:
    st.image("2-gif.gif", caption='Verse Exchange, Alarm, Invitation')
with colr:
    st.video("2-talk.mp4")
st.caption("In the evening, Yingying and Hongniang went to the garden to burn incense. When Zhang Sheng saw them, he recited a poem, and Yingying praised it sincerely.")
st.caption("Soon after, Sun Feihu heard of Yingying's beauty and brought men to rob the temple. Mrs. Cui said she would betroth Yingying to the man who rescued them. Zhang Sheng succeeded in helping the temple out of trouble.")
st.caption("Mrs. Cui invites Zhang Sheng to a banquet. Zhang Sheng is very excited as he thinks that Mrs. Cui agrees to marry him and Yingying.")
st.caption("  ")
st.caption("  ")

coll, colr = st.columns(2)
# Example Image
with coll:
    st.image("3-gif.gif", caption='The Promise Broken, The Lute, First Expectation, The Billet-Doux')
with colr:
    st.video("3-talk.mp4")
st.caption("At the banquet, however, Mrs Cui wanted Yingying to be brother and sister with Zhang Sheng. Zhang Sheng is shocked; Yingying also expresses her deep dissatisfaction.")
st.caption("From then on, Zhang Sheng was sad and played the guqin in front of the window every night.Yingying couldn't help but shed tears as she listened it.")
st.caption("When Zhang Sheng fell ill as a result, Yingying asked Hongniang to send a letter, hinting to Zhang Sheng that she will meet him in the garden.")
st.caption("Hongniang is dissatisfied that Yingying did not tell her but secretly met with Zhang Sheng. That night, they went to the garden to burn incense and saw Zhang Sheng jumping off the wall.")
st.caption("  ")
st.caption("  ")

coll, colr = st.columns(2)
# Example Image
with coll:
    st.image("4-gif.gif", caption='Repudiation, Illness, Further Expectation')
with colr:
    st.video("4-talk.mp4")
st.caption("Unexpectedly, Yingying could only blame Zhangsheng because Hongniang, saying that since he was already brother and sister to her, why did he come to meet her again.")
st.caption("Zhang Sheng could not withstand this torture and was too sick to get out of bed from the next day.")
st.caption("Worried about Zhang Sheng, Yingying asked Hongniang to send him another letter, saying she would come to see him at night. Zhang Sheng was very happy.")
st.caption("  ")
st.caption("  ")

coll, colr = st.columns(2)
# Example Image
with coll:
    st.image("5-gif.gif", caption='Tryst, Rose in The Dock, Farewell Feast')
with colr:
    st.video("5-talk.mp4")
st.caption("At night, Yingying came and Zhang Sheng opened the door for her. The two poor lovers were finally together.")
st.caption("Then Mrs. Cui knew about it. She tortured Hongniang, who reproached her for not keeping her word. Mrs. Cui had no choice but to ask Zhang Sheng to take the examination to become an official so that he could come back to marry Yingying.")
st.caption("Zhang Sheng was forced to go to Chang'an to take the examination. The two lovers waved goodbye in tears. Later, Zhang Sheng successfully passed the test and eventually married Yingying.")
st.caption("  ")
st.caption("  ")

# 合成图板块
st.markdown("</br>", unsafe_allow_html=True)
st.markdown(
    "<b> <i> A Meeting Across Millennia? ", unsafe_allow_html=True)
st.caption("The love between Cui Yingying and Zhang Sheng took many twists and turns, but fortunately, the lovers were finally reunited.")
st.caption("If there was a time machine, and Cui Yingying and Zhang Sheng in Wang Shuhui's painting came to modern times, and put on the modern improved Chinese dress and traveled together in the ancient town, what kind of traces would be left behind?")
st.caption("Perhaps they would have taken photos like this——")
st.image("photo.png")

st.caption("  ")
st.caption("  ")
st.caption("We hope to make Wang Shuhui's paintings move through ai's technology, so that readers can see a vivid version of The Romance of the West Chamber and trigger deeper emotional resonance.")


# -------------Sidebar Section------------------------------------------------
#这一段是左侧边栏展示的内容
#这里开始侧边栏设计
with st.sidebar:
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

