import numpy as np
import streamlit as st
import datetime


def get_week_display(week):
    # 현재 날짜와 시간을 가져옵니다
    now = datetime.datetime.now()
    week_ago = now - datetime.timedelta(weeks=week)
    # 현재 날짜가 속한 주의 첫 번째 날 (월요일)을 가져옵니다
    start_of_week = week_ago - datetime.timedelta(days=week_ago.weekday())

    # 이번 주가 몇 번째 주인지를 계산합니다
    week_number = (start_of_week.day - 1) // 7 + 1
    display = f"{start_of_week.year}년 {start_of_week.month}월 {week_number}주차"
    return display


st.title('lineage m')
st.markdown('----')

# st.header('[라인 이전 결과]')

# week_number = [get_week_display(0), get_week_display(1), get_week_display(2), get_week_display(3)]

# select_week = st.selectbox('Select', week_number)
col1, col2, col3 = st.columns(3)
# st.write(select_week)
with col1:
    col1.subheader('켄라:케레')
    col1.write(':blue[탑], :blue[우주], 돌격')
    col1.subheader('파푸:질리언')
    col1.write(':red[왕]')
    col1.subheader('데스:아툰')
    col1.write(':red[PK]')

with col2:
    col2.subheader('안타:하딘')
    col2.write(':blue[탑(와우귤귤)]')
    col2.subheader('데포:이실')
    col2.write(':blue[탑(대장)] :red[악동(핵킬)]')
    col2.subheader('발라:군터')
    col2.write(':blue[빛(소닉), 난],:red[각성, 돌격]')

with col3:
    col3.subheader('판도라:라바')
    col3.write(':blue[탑(그리가딘) 우주(짐승)] 태극기')
    col3.subheader('린드:사이하')
    col3.write(':red[A]')
    col3.subheader('듀크:블루')
    col3.write(':red[헉]')

# Display a chat input widget.
# st.chat_input("Say something")