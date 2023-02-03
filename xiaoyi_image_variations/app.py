import streamlit as st

import os
import openai
from PIL import Image
# openai.api_key = os.environ.get('openai.api_key')

# 页面设置
st.set_page_config(
    page_title="小译学长|一张原图生成多张不同图",
    page_icon=":robot:"
)
st.header("🔥AI一张原图生成多张不同图")

#检查账号登陆
def get_text1():
    if 'openai_key' not in st.session_state:
        input_text1 = st.text_input("📫请输入你的账号: ", key="input")
        if st.button("确认登陆！", key="input3"):
            st.session_state['openai_key'] = input_text1
            return input_text1
    else:
        return st.session_state['openai_key']

openai_key = get_text1()
if openai_key:
    openai.api_key = openai_key
    st.write("")
else:
    st.write("⚒️账号获取方式：扫描下方二维码或搜索关注微信公众号【正经人王同学】回复【小译学长】获取你的账号，然后将公共账号输入到此处，再两次点击【确认登陆！】就好")
    st.image('https://pic4.zhimg.com/v2-401dd67cf027f85f53e4be3bd28dab5f_b.jpg')
st.markdown("""[正经人王同学|公众号](https://mp.weixin.qq.com/s?__biz=Mzg3ODcwNzk3Nw==&mid=2247485615&idx=1&sn=c691d496386b5972e36fea8eaee33b97&chksm=cf0edcc9f87955df95fa23a716d78d496e7456183da7cfa6b348db6988865da9060896abcdcd&token=1164458978&lang=zh_CN#rd) [抖音](https://www.douyin.com/user/MS4wLjABAAAAIdY0VlMSK0Shyd4FxHBgkXAtH4Zq8wsuKzIuSICWpy0) [小红书 ](https://www.xiaohongshu.com/user/profile/5f12a46a000000000101ff27)""")
uploaded_image = st.file_uploader("🌈小译学长温馨提示：你可以上传一张喜欢的图像，并根据原始图像的灵感创造出不同的变化图像", type=["jpg", "png","jpeg"])

if uploaded_image is not None:
    # Convert image to png format
    img = Image.open(uploaded_image)

    #rize the photo
    img_width, img_height = img.size
    if img_width != img_height:
        img_size = min(img_width, img_height)
        img = img.crop((0, 0, img_size, img_size))

  
    
   
    img.save("origin.png")

    st.image("origin.png", caption='Uploaded image', use_column_width=True)

 
def image_variation():
    try:
        images = openai.Image.create_variation(
            image=open("origin.png", "rb"),
            n=4,
            size="1024x1024"
        )
        st.empty()
        for image in images["data"]:
            st.image(image["url"],width=300)
    except Exception as e:
          st.write("❌❌❌你的账号填写有误，请刷新页面重新填写正确的账号！")

if st.button("开始绘画"):
    image_variation()


st.write("""
### 上传图片前必看！：

👀上传图像必须满足以下要求：\n
1、支持上传的图像格式有jpg、jpeg、png\n
2、大小小于4MB\n
可用tinypng压缩原图像大小，地址：https://tinypng.com/


""")

