import streamlit as st
from streamlit_chat import message
import os
import openai

#页面设置
st.set_page_config(
    page_title="小译学长|AI对话一问一答模式",
    page_icon=":robot:"
)
st.header("🔥AI对话一问一答模式")

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

# openAI code
def openai_create(prompt):
    try:

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )

        return response.choices[0].text

    # except openai.error.UnauthorizedError:
    #     return "API Key不正确，请输入正确的API Key。"
    # except openai.error.RateLimitError:
    #     Error="当前小译学长访问量过大，请过一段时间再试！开发者正在努力扩张服务能力，敬请期待！"
    #     return Error

    except Exception as e:
        return "你的账号填写有误，请刷新页面重新填写正确的账号！"


def chatgpt_clone(input):
    output = openai_create(input)
    return output

#  Streamlit App
# st.set_page_config(
#     page_title="小译AI对话单轮版",
#     page_icon=":robot:"
# )




# st.header("🏅和小译学长聊聊天")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("📫请告诉小译学长你想说的吧: ", key="input1")
    if st.button("发送", key="input2"):
        return input_text
    return None

st.markdown("""[正经人王同学|公众号](https://mp.weixin.qq.com/s?__biz=Mzg3ODcwNzk3Nw==&mid=2247485615&idx=1&sn=c691d496386b5972e36fea8eaee33b97&chksm=cf0edcc9f87955df95fa23a716d78d496e7456183da7cfa6b348db6988865da9060896abcdcd&token=1164458978&lang=zh_CN#rd) [抖音](https://www.douyin.com/user/MS4wLjABAAAAIdY0VlMSK0Shyd4FxHBgkXAtH4Zq8wsuKzIuSICWpy0) [小红书 ](https://www.xiaohongshu.com/user/profile/5f12a46a000000000101ff27)""")

user_input = get_text()

if user_input:
     
    output = chatgpt_clone(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
