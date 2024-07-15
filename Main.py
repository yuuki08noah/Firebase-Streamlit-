import streamlit as st;
st.write("자료구조와 알고리즘 : **Queue 와 Priority Queue**")

text = st.text_input('학번과 이름을 입력하세요 : ')
if st.button('저장'):
    if 'name' not in st.session_state:
        st.session_state.name = text
    else:
        st.session_state.name = text