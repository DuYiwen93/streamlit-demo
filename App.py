
import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO
#from API import transfer_style


#这里改标题，page title后面的引号内容是标题，icon里面是网页标志
st.set_page_config(page_title="PixelMix - Style Transfer",
                   page_icon="./assets/favicon.png", layout="centered")

# -------------Header Section------------------------------------------------

title = '<p style="text-align: center;font-size: 50px;font-weight: 350;font-family:Cursive "> PixelMix </p>'
st.markdown(title, unsafe_allow_html=True)

# CSS来改变背景色
#https://htmlcolorcodes.com/zh/ 这个网站上找一个想要的背景色把井号的代码复制到下面这一小段的background color后面
def set_bg_color():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #F996F1;
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
    "<b> <i> Create Digital Art using Machine Learning ! </i> </b>  &nbsp; We takes 2 images — Content Image & Style Image — and blends "
    "them together so that the resulting output image retains the core elements of the content image, but appears to "
    "be “painted” in the style of the style reference image.", unsafe_allow_html=True
)




#下面这一大段是主要的展示部分，coll是左边的一列，colr是右边的一列，默认展示动图，如果太小自行在外面放大（就是把动图本身放大），别试着在网页里放大，st容器有问题，caption对应的是每一列的文字部分
#默认展示动图，如果要展示视频就取消colr下面两行的注释，并且注释掉最上面一行
coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("./materials/1-talk.mp4")
    st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
#st.image(image="./assets/nst.png")
with colr:
    st.image("./materials/video/1-gif.gif", caption='我也不知道这是啥但是好像传gif就是这么简单')
    # st.video("./materials/video/1-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("./materials/2-talk.mp4")
    st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
#st.image(image="./assets/nst.png")
with colr:
    st.image("./materials/video/2-gif.gif", caption='我也不知道这是啥但是好像传gif就是这么简单')
    # st.video("./materials/video/2-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("./materials/3-talk.mp4")
    st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
#st.image(image="./assets/nst.png")
with colr:
    st.image("./materials/video/3-gif.gif", caption='我也不知道这是啥但是好像传gif就是这么简单')
    # st.video("./materials/video/3-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("./materials/4-talk.mp4")
    st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
#st.image(image="./assets/nst.png")
with colr:
    st.image("./materials/video/4-gif.gif", caption='我也不知道这是啥但是好像传gif就是这么简单')
    # st.video("./materials/video/4-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
coll, colr = st.columns(2)
# Example Image
with coll:
    st.video("./materials/5-talk.mp4")
    st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")
#st.image(image="./assets/nst.png")
with colr:
    st.image("./materials/video/5-gif.gif", caption='我也不知道这是啥但是好像传gif就是这么简单')
    # st.video("./materials/video/5-MP4.mp4")
    # st.caption("我也不知道为啥视频的caption加的这么下面但是好像传视频也蛮简单的")

st.markdown("</br>", unsafe_allow_html=True)





# -------------Sidebar Section------------------------------------------------
#这一段是左侧边栏展示的内容
#这里开始侧边栏设计
with st.sidebar:
    #这一一坨里面放的东西展示在最上面，呈一列展示
    #替换掉下方引号里的中文内容 切记是中文内容，别乱删别的
    st.image(image="./assets/speed-brush.gif")
    st.markdown("</br>", unsafe_allow_html=True)

    st.markdown('<p style="font-size: 25px;font-weight: 550;">这里放作者信息？ 🎨</p>',
                unsafe_allow_html=True)
    st.markdown('这里放点什么呢，简介？',
                unsafe_allow_html=True)



    # ---------------------Example art images------------------------------
    #这里展开侧边栏的两列设计，example里放的是图，如果不需要两列的设计就把这一大段全部注释掉，在上面单栏的地方加内容
    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content1.jpg")
    with col2:
        st.image(image="./assets/art1.png")

    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content2.jpg")
    with col2:
        st.image(image="./assets/art2.png")

    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content3.jpg")
    with col2:
        st.image(image="./assets/art3.png")

    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content4.jpg")
    with col2:
        st.image(image="./assets/art4.png")








#这一团是作者（这篇网页设计的作者）的个人信息，如果不要全部注释掉，要的话适当改其中内容
 # ----------------------------------------------------------------------

    # line break
    st.markdown(" ")
    # About the programmer
    st.markdown("## Made by **Deepesh Mhatre** \U0001F609")
    st.markdown("Contribute to this project at "
                "[*github.com/deepeshdm*](https://github.com/deepeshdm/Realtime_Face_Detection)")





#这团别管，嫌烦全部删掉
# # -------------Body Section------------------------------------------------

# # Upload Images
# col1, col2 = st.columns(2)
# content_image = None
# style_image = None
# with col1:
#     content_image = st.file_uploader(
#         "Upload Content Image (PNG & JPG images only)", type=['png', 'jpg'])
# with col2:
#     style_image = st.file_uploader(
#         "Upload Style Image (PNG & JPG images only)", type=['png', 'jpg'])


# st.markdown("</br>", unsafe_allow_html=True)
# st.warning('NOTE : You need atleast Intel i3 with 8GB memory for proper functioning of this application. ' +
#    ' Images greater then (2000x2000) are resized to (1000x1000).')


# if content_image is not None and style_image is not None:

#     with st.spinner("Styling Images...will take about 20-30 secs"):

#         content_image = Image.open(content_image)
#         style_image = Image.open(style_image)

#         # Convert PIL Image to numpy array
#         content_image = np.array(content_image)
#         style_image = np.array(style_image)

#         # Path of the pre-trained TF model
#         model_path = r"model"

#         # output image
#         styled_image = transfer_style(content_image, style_image, model_path)
#         if style_image is not None:
#             # some baloons
#             st.balloons()

#         col1, col2 = st.columns(2)
#         with col1:
#             # Display the output
#             st.image(styled_image)
#         with col2:

#             st.markdown("</br>", unsafe_allow_html=True)
#             st.markdown(
#                 "<b> Your Image is Ready ! Click below to download it. </b>", unsafe_allow_html=True)

#             # de-normalize the image
#             styled_image = (styled_image * 255).astype(np.uint8)
#             # convert to pillow image
#             img = Image.fromarray(styled_image)
#             buffered = BytesIO()
#             img.save(buffered, format="JPEG")
#             st.download_button(
#                 label="Download image",
#                 data=buffered.getvalue(),
#                 file_name="output.png",
#                 mime="image/png")
