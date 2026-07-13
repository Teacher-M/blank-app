import streamlit as st

st.title("📈 이차함수 그래프 그리기")

st.write("함수의 계수를 정하고, 표를 완성한 뒤 그래프를 확인해 보세요.")

# 계수 정하기
a = st.slider("a의 값", -3, 3, 1)
b = st.slider("b의 값", -5, 5, 0)
c = st.slider("c의 값", -5, 5, 0)

if a == 0:
    st.warning("a가 0이면 이차함수가 아닙니다. a를 0이 아닌 값으로 바꿔 주세요.")
    st.stop()

st.subheader("현재 이차함수")

st.latex(f"y = {a}x^2 + {b}x + {c}")

st.write("각 x값에 알맞은 y값을 계산하여 입력하세요.")

# 사용할 x값
x_values = list(range(-5, 6))

student_answers = []

# 학생이 y값 입력
for x in x_values:
    answer = st.number_input(
        f"x = {x}일 때 y의 값",
        value=0,
        step=1,
        key=f"answer_{x}"
    )
    student_answers.append(answer)

# 확인 버튼
if st.button("정답과 그래프 확인하기"):

    correct_answers = []

    for x in x_values:
        y = a * x**2 + b * x + c
        correct_answers.append(y)

    st.subheader("✅ 계산 결과")

    score = 0

    for i in range(len(x_values)):
        x = x_values[i]
        student_y = student_answers[i]
        correct_y = correct_answers[i]

        if student_y == correct_y:
            st.success(f"x = {x}: 정답입니다! y = {correct_y}")
            score += 1
        else:
            st.error(
                f"x = {x}: 입력한 값은 {student_y}, "
                f"정답은 {correct_y}입니다."
            )

    st.info(f"총 {len(x_values)}문제 중 {score}문제를 맞혔습니다.")

    st.subheader("📊 이차함수 그래프")

    # Streamlit 기본 그래프로 나타내기
    graph_data = {
        "x": x_values,
        "y": correct_answers
    }

    st.line_chart(
        graph_data,
        x="x",
        y="y"
    )

    st.subheader("좌표 확인")

    for x, y in zip(x_values, correct_answers):
        st.write(f"({x}, {y})")

    if a > 0:
        st.write("이 그래프는 아래로 볼록한 포물선입니다.")
    else:
        st.write("이 그래프는 위로 볼록한 포물선입니다.")

st.divider()

st.write(
    "💡 활동 방법: 먼저 활동지나 공책에 좌표를 찍어 "
    "그래프를 그린 뒤, 웹 앱의 그래프와 비교해 보세요."
)