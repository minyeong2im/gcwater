import streamlit as st

# 제목
st.title("💧 수도요금 계산 프로그램")

# 입력 영역
st.header("📥 입력값")
수용가번호 = st.text_input("수용가 번호")
성명 = st.text_input("성명")
업종 = st.selectbox("업종 선택", ["가정용", "일반용", "대중탕용", "전용공업용", "산업용"])
사용량 = st.number_input("사용량 (톤)", min_value=0, step=1)
검침구분 = st.radio("검침 구분", ["매월(1)", "격월(2)"])
세대수 = st.number_input("세대수", min_value=1, step=1)
하수도여부 = st.checkbox("하수도 부과 여부")

# 버튼
if st.button("💡 요금 계산하기"):
    # 아주 간단한 더미 계산 (실제 로직 대신 예시용)
    기본요금 = 1000  
    사용요금 = 사용량 * 420 if 업종 == "가정용" else 사용량 * 727
    하수도요금 = 사용량 * 300 if 하수도여부 else 0
    총요금 = 기본요금 + 사용요금 + 하수도요금

    # 출력 영역
    st.header("📊 계산 결과")
    st.write(f"**수용가 번호**: {수용가번호}")
    st.write(f"**성명**: {성명}")
    st.write(f"**업종**: {업종}")
    st.write(f"**검침 구분**: {검침구분}")
    st.write(f"**세대수**: {세대수}")
    st.write(f"**총 요금**: {총요금:,} 원")