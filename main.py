import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

from time import sleep

st.set_page_config(initial_sidebar_state="collapsed")

parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "cubes.svg")
options = {
    "show_menu": False,
    "show_sidebar": False,
}

### WORK WITH JS
from streamlit_js_eval import streamlit_js_eval
# Hide JS output as empty space at the top
st.markdown(
    """
    <style>
        .element-container:has(
            iframe[title="streamlit_js_eval.streamlit_js_eval"]
        ) {
            display: none
        }
    </style>
    """,
    unsafe_allow_html=True,
)

styles = {
    "nav": {
        "background-color": "black",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
pages_left = ["ctOS"]
pages_right = ["About", "Download"]
urls = {"Download": "https://example.com"}

width = 0
while True:
	try:
		width = int(streamlit_js_eval(js_expressions='screen.width', key = 'SCR'))
		break
	except:
		sleep(0.05)

# Pages at the left
pages = [] + pages_left

size = 342.75
# st - 154
# end - 188.75
# all - 342.75
# separator size - 33.6
while (size + 33.6) < width:
	pages.append(" ")
	size += 33.6

pages += pages_right

page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    "Home": pg.home,
    "About": pg.about,
}
go_to = functions.get(page)
if go_to:
    go_to()
