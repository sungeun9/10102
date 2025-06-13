import streamlit as st

# 운세를 이름 길이 기준으로 간단하게 생성하는 함수
def get_fortune(name):
    length = len(name)
    if length <= 2:
        return "짧은 이름을 가진 당신은 결단력과 집중력이 뛰어납니다!"
    elif length <= 4:
        return "균형 잡힌 이름의 당신은 대인관계가 원만하고 행운이 따릅니다!"
    else:
        return "긴 이름을 가진 당신은 창의력과 끈기가 강합니다!"

# Streamlit 앱
st.title("이름으로 보는 운세")

name = st.text_input("이름을 입력하세요:")

if name:
    fortune = get_fortune(name)
    st.success(f"{name} 님의 운세: {fortune}")
else:
    st.info("이름을 입력하면 운세를 알려드립니다.")
