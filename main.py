import streamlit as st
from datetime import datetime

def get_horoscope(month, day):
    # 월/일 기준 간단한 운세 메시지 예시
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "양자리: 오늘은 새로운 시작이 좋은 날입니다!"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "황소자리: 꾸준함이 행운을 가져다줄 거예요."
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "쌍둥이자리: 소통이 중요한 하루입니다."
    # ... 간단히 12별자리 중 몇 개만 넣었음
    else:
        return "오늘은 평범한 하루, 자신감을 가지세요!"

st.title("생일로 보는 간단 운세")

birthday = st.date
