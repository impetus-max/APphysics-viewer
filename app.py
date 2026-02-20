import base64
from pathlib import Path

import streamlit as st

st.set_page_config(layout="wide")

APP_DIR = Path(__file__).resolve().parent

def display_pdf(pdf_path: Path):
    if not pdf_path.exists():
        st.error(f"PDF 파일을 찾을 수 없습니다: {pdf_path.name}")
        st.info("해결: PDF 파일을 리포지토리에 추가하고 app.py와 같은 폴더에 두거나, 파일명을 코드와 일치시키세요.")
        return

    try:
        data = pdf_path.read_bytes()
        base64_pdf = base64.b64encode(data).decode("utf-8")
        # toolbar=0 : 다운로드/인쇄 메뉴 숨김(뷰어에 따라 완전히 숨겨지지 않을 수도 있음)
        pdf_display = (
            f'<iframe src="data:application/pdf;base64,{base64_pdf}#toolbar=0" '
            f'width="100%" height="800" type="application/pdf"></iframe>'
        )
        st.markdown(pdf_display, unsafe_allow_html=True)
    except Exception as e:
        st.exception(e)

st.title("고급 물리학 수업 전용 뷰어")

# app.py 기준 경로로 고정
display_pdf(APP_DIR / "lesson_01.pdf")