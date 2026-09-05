import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

st.title("専門家AI相談アプリ")

st.write("##### このアプリについて")
st.write("選択した専門家の視点から、生成AIが質問に回答します。")

st.write("##### 操作方法")
st.write("1. 相談したい専門家をラジオボタンで選択してください。")
st.write("2. 質問を入力フォームに入力してください。")
st.write("3. 「実行」ボタンを押すと、回答が表示されます。")

selected_item = st.radio(
    "相談したい専門家を選択してください。",
    ["料理の専門家", "筋トレの専門家"]
)

st.divider()

input_message = st.text_input(label="質問を入力してください。")


def get_llm_answer(input_text, selected_expert):
    if selected_expert == "料理の専門家":
        system_message = "あなたは料理の専門家です。家庭料理のレシピや調理のコツについて、分かりやすく丁寧に回答してください。"
    else:
        system_message = "あなたは筋トレの専門家です。トレーニング方法や体づくりについて、安全に配慮した上で分かりやすく回答してください。"

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]

    result = llm(messages)
    return result.content


if st.button("実行"):
    st.divider()

    if input_message:
        answer = get_llm_answer(input_message, selected_item)
        st.write("##### 回答")
        st.write(answer)

    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")