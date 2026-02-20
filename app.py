import streamlit as st
import base64

st.set_page_config(layout="wide")

def display_pdf(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # toolbar=0 설정으로 다운로드/인쇄 메뉴를 숨깁니다.
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#toolbar=0" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

st.title("고급 물리학 수업 전용 뷰어")
display_pdf("lesson_01.pdf") # 여기에 업로드한 PDF 파일명을 쓰세요.