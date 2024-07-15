import streamlit as st
st.write(st.session_state.name)
score=0
if(st.session_state.anschs=='Heap'):
    score+=50
if(st.session_state.anstxt=='2'):
    score+=50
st.session_state.score=score
st.write(score)