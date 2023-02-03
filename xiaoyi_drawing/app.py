import streamlit as st
import os
import openai

# openai.api_key = os.environ.get('openai.api_key')
# openai.api_key ="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"
#页面设置
st.set_page_config(
    page_title="小译学长|AI绘画（输入文本描述可生成对应图）",
    page_icon=":robot:"
)
st.header("🔥AI绘画（输入文本描述可生成对应图）")

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
prompt = st.text_input("📝告诉小译学长你想画的图是什么样的吧:")

def image(prompt):
  try:
    images = openai.Image.create(
      prompt=prompt,
      n=4,
      size="1024x1024"
    )
    st.empty()
    for image in images["data"]:
      st.image(image["url"],width=300)
    return
  except Exception as e:
          st.write("❌❌❌你的账号填写有误，请刷新页面重新填写正确的账号！")
if st.button("开始绘画"):


  image(prompt)  




st.write("""
### 文本生成图技巧：

👀描述词格式：主体（描述的是什么）+环境（在什么样的环境下）+风格（图片的风格是什么：二次元、古风、钢笔画等等）

✏️描述词例子：上海外滩，白色背景，线稿，钢笔画，速写，4K,未来主义
""")