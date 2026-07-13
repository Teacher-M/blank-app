import streamlit as st

st.title("이차함수 값 알아보기")

st.write("계수를 바꾸어 이차함수의 값을 확인해 보세요.")

a = st.slider("a의 값", -5, 5, 1)
b = st.slider("b의 값", -10, 10, 0)
c = st.slider("c의 값", -10, 10, 0)
x = st.slider("x의 값", -10, 10, 0)

y = a * x**2 + b * x + c

st.subheader("현재 이차함수")

st.write(f"y = {a}x² + {b}x + {c}")

st.subheader("계산 결과")

st.write(f"x = {x}일 때")
st.success(f"y = {y}")

if a > 0:
    st.write("그래프는 아래로 볼록합니다.")
elif a < 0:
    st.write("그래프는 위로 볼록합니다.")
else:
    st.warning("a가 0이므로 이차함수가 아닙니다.")