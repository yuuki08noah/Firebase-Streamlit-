import streamlit as st
choice = st.radio("우선순위 큐를 구현하는 방법으로 가장 적합한 것은? ", ["HashMap", "Heap", "Queue", "Stack", "LinkedList"])

text = st.text_input("queue<int> arr; arr.push(2); arr.push(3); arr.pop(); arr.push(4); cout << arr.size();의 출력을 입력하세요")

if st.button('제출'):
    st.session_state.anstxt=text
    st.session_state.anschs=choice